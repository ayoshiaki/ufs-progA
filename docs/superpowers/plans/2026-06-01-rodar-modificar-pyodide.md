# Migrar Rodar/Modificar para Pyodide — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Tirar as fases **Rodar** e **Modificar** do autograder server-side (`exec`) e passá-las a rodar no **Pyodide (navegador)**, como já acontece no **Criar** — eliminando o uso de CPU/RAM do servidor com código de aluno e o risco de laço infinito travar o servidor para a turma toda.

**Architecture:** Adicionar um helper `exercicio_saida_sandbox` em `utils/sandbox_pyodide.py` que executa o programa do aluno no Pyodide, **captura o stdout** e compara com o esperado (sem UI de comprovante — Rodar/Modificar não entregam nada). Trocar as 32 páginas (`02_rodar.py`/`04_modificar.py` dos 16 temas) de `exercicio_saida` (server-side) para `exercicio_saida_sandbox`. O `autograder.py`/`componentes.py` continuam existindo (usados pelos testes), mas saem do caminho de execução em produção.

**Tech Stack:** Python 3.11, Streamlit, `streamlit.components.v1` (HTML), Pyodide (CPython em WebAssembly), testes sem framework (scripts `python tests/test_*.py`).

**Contexto verificado (jun/2026):** 32 páginas usam `exercicio_saida` (35 chamadas); **nenhuma usa `stdin_text`**; nenhuma usa `exercicio_funcao` (server-side). O Criar já roda em Pyodide via `exercicio_*_sandbox`. Interpretador com `streamlit_book` instalado: `/usr/local/bin/python3.11`.

---

## File Structure

- **Modify** `utils/sandbox_pyodide.py` — adicionar `_HTML_SAIDA` (template) e `exercicio_saida_sandbox()`. Espelha o template `_HTML_EXPR` existente, mas captura stdout e **não** tem UI de entrega/comprovante.
- **Modify** 32 páginas `pages/*/02_rodar.py` e `pages/*/04_modificar.py` — trocar import e chamada de `exercicio_saida` → `exercicio_saida_sandbox`.
- **Create** `tests/test_saida_sandbox.py` — (a) integridade de conteúdo: para cada chamada migrada, os modelos de **Rodar** produzem o `esperado` e os de **Modificar** **não** produzem (estão quebrados de propósito); (b) contrato do runner: replica em CPython a lógica "exec + captura stdout + compara strip".
- **Modify** `README.md` — atualizar a seção "Segurança do autograder": Rodar/Modificar agora rodam no navegador; o autograder server-side só é exercitado pelos testes.
- **No change** em `utils/autograder.py` e `utils/componentes.py` (mantidos para os testes e compatibilidade).

---

### Task 1: Teste de integridade de conteúdo (guarda da migração)

Escrito primeiro: passa **antes** da migração (lê `modelo`/`esperado` independentemente do helper) e **continua passando depois**, garantindo que a troca mecânica não corrompeu nenhum exercício. Reconhece tanto `exercicio_saida` quanto `exercicio_saida_sandbox`.

**Files:**
- Test: `tests/test_saida_sandbox.py`

- [ ] **Step 1: Escrever o teste de integridade de conteúdo**

```python
"""
Testa o conteúdo das fases Rodar/Modificar (independente de rodarem no servidor
ou no Pyodide): extrai `modelo` e `esperado` de cada exercício por AST e roda o
modelo em CPython capturando o stdout.

- Rodar (02_rodar.py): o modelo é "só rodar" → seu stdout DEVE ser o esperado.
- Modificar (04_modificar.py): o modelo está quebrado de propósito → seu stdout
  NÃO deve ser o esperado (ou ele lança erro).

Reconhece tanto `exercicio_saida` (server-side, antes da migração) quanto
`exercicio_saida_sandbox` (Pyodide, depois). Rode direto:

    /usr/local/bin/python3.11 tests/test_saida_sandbox.py
"""

import ast
import io
import contextlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAGES = RAIZ / "pages"
NOMES = {"exercicio_saida", "exercicio_saida_sandbox"}


def _exercicios(arquivo):
    """Lista (modelo, esperado) de cada chamada de exercicio_saida[_sandbox]."""
    achados = []
    arvore = ast.parse(arquivo.read_text())
    for node in ast.walk(arvore):
        if isinstance(node, ast.Call) and getattr(node.func, "id", None) in NOMES:
            kw = {k.arg: k.value for k in node.keywords}
            if "modelo" in kw and "esperado" in kw:
                achados.append((ast.literal_eval(kw["modelo"]),
                                ast.literal_eval(kw["esperado"])))
    return achados


def _stdout(codigo):
    """Roda o código em CPython e devolve (saida_strip, erro_ou_None)."""
    ns = {}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(codigo, ns)
        return buf.getvalue().strip(), None
    except Exception as e:  # modelo de Modificar pode lançar — é "quebrado"
        return buf.getvalue().strip(), repr(e)


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


def test_modelos_de_rodar_produzem_o_esperado():
    for f in sorted(PAGES.glob("*/02_rodar.py")):
        for i, (modelo, esperado) in enumerate(_exercicios(f)):
            saida, erro = _stdout(modelo)
            rotulo = f"{f.parent.name}/02_rodar[{i}]"
            if erro:
                print(f"    {rotulo} erro inesperado: {erro}")
            _ok(f"{rotulo}: modelo imprime o esperado",
                erro is None and saida == str(esperado).strip())


def test_modelos_de_modificar_estao_quebrados():
    for f in sorted(PAGES.glob("*/04_modificar.py")):
        for i, (modelo, esperado) in enumerate(_exercicios(f)):
            saida, erro = _stdout(modelo)
            rotulo = f"{f.parent.name}/04_modificar[{i}]"
            # "Quebrado" = lança erro OU imprime algo diferente do esperado.
            quebrado = (erro is not None) or (saida != str(esperado).strip())
            _ok(f"{rotulo}: modelo está quebrado de propósito", quebrado)


if __name__ == "__main__":
    test_modelos_de_rodar_produzem_o_esperado()
    test_modelos_de_modificar_estao_quebrados()
    print("\n🎉 conteúdo de Rodar/Modificar OK")
```

- [ ] **Step 2: Rodar e confirmar que passa já (antes da migração)**

Run: `/usr/local/bin/python3.11 tests/test_saida_sandbox.py`
Expected: PASS (todos ✅). Se algum Modificar falhar em "está quebrado", é um problema de conteúdo pré-existente — pare e investigue antes de migrar.

- [ ] **Step 3: Commit**

```bash
git add tests/test_saida_sandbox.py
git commit -m "test: guarda de conteúdo das fases Rodar/Modificar"
```

---

### Task 2: Helper `exercicio_saida_sandbox` (Pyodide, captura stdout)

**Files:**
- Modify: `utils/sandbox_pyodide.py` (acrescentar ao final, após `exercicio_script_sandbox`)
- Test: `tests/test_saida_sandbox.py` (acrescentar um teste do contrato do runner)

- [ ] **Step 1: Escrever o teste do contrato do runner**

Acrescente em `tests/test_saida_sandbox.py`, ANTES do bloco `if __name__`:

```python
def _runner_contrato(codigo, esperado):
    """Réplica em CPython da lógica do RUNNER do Pyodide (exec + stdout + strip)."""
    ns = {}
    buf = io.StringIO()
    erro = None
    ok = False
    try:
        with contextlib.redirect_stdout(buf):
            exec(codigo, ns)
        ok = buf.getvalue().strip() == esperado.strip()
    except Exception as e:
        erro = repr(e)
    return ok, buf.getvalue(), erro


def test_contrato_do_runner():
    ok, saida, erro = _runner_contrato("print('Total:', 5 * 3)", "Total: 15")
    _ok("saída correta → ok=True, sem erro", ok and erro is None)
    _ok("captura o stdout", saida.strip() == "Total: 15")
    ok2, _s, _e = _runner_contrato("print(10)", "20")
    _ok("saída errada → ok=False", not ok2)
    ok3, _s, erro3 = _runner_contrato("1/0", "x")
    _ok("exceção → ok=False e erro preenchido", (not ok3) and erro3 is not None)
```

E adicione a chamada no `__main__`:

```python
    test_contrato_do_runner()
```

- [ ] **Step 2: Rodar e ver falhar? Não — este teste valida lógica pura CPython e já passa**

Run: `/usr/local/bin/python3.11 tests/test_saida_sandbox.py`
Expected: PASS. (O `test_contrato_do_runner` documenta o comportamento que o RUNNER do Pyodide deve reproduzir; serve de especificação para o Step 3.)

- [ ] **Step 3: Implementar o helper no `utils/sandbox_pyodide.py`**

Acrescente ao final do arquivo (depois de `exercicio_script_sandbox`):

```python
# ---------------------------------------------------------------------------
# Variante por SAÍDA — para as fases Rodar/Modificar. Roda o PROGRAMA do aluno
# no Pyodide, captura o stdout e compara com o esperado. NÃO tem comprovante
# (Rodar/Modificar não entregam nada). Substitui o exercicio_saida server-side.
# ---------------------------------------------------------------------------

_HTML_SAIDA = Template(r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 0; color: #1a1a1a; }
  textarea { width: 100%; box-sizing: border-box; font-family: ui-monospace, Menlo, Consolas, monospace;
             font-size: 14px; padding: 10px; border: 1px solid #ccc; border-radius: 8px; }
  button { font-size: 14px; padding: 8px 16px; border: 0; border-radius: 8px;
           background: #ff4b4b; color: #fff; cursor: pointer; margin-top: 8px; }
  button:disabled { background: #bbb; cursor: not-allowed; }
  .ok { color: #137333; } .fail { color: #c5221f; }
  .status { margin-top: 10px; font-size: 14px; }
  pre { background: #f0f0f0; padding: 10px; border-radius: 8px; font-size: 13px;
        white-space: pre-wrap; word-break: break-word; }
  code { background: #f0f0f0; padding: 1px 4px; border-radius: 4px; }
  .rotulo { font-size: 13px; color: #555; margin-top: 12px; }
</style>
</head>
<body>
  <textarea id="code" rows="10">$MODELO</textarea>
  <div><button id="run">Rodar e verificar (sandbox)</button>
       <span class="status" id="status"></span></div>
  <div class="rotulo">Saída do seu programa:</div>
  <pre id="saida">(rode para ver)</pre>
  <div id="erro"></div>

<script src="https://cdn.jsdelivr.net/pyodide/v$PYVER/full/pyodide.js"></script>
<script>
var EXPECTED = $ESPERADO;
var pyodideReady = null;

function getPyodide() {
  if (!pyodideReady) { pyodideReady = loadPyodide(); }
  return pyodideReady;
}

var RUNNER = [
  "import io, json, contextlib, traceback",
  "ns = {}",
  "buf = io.StringIO()",
  "ok = False; erro = None",
  "try:",
  "    with contextlib.redirect_stdout(buf):",
  "        exec(STUDENT_CODE, ns)",
  "    saida = buf.getvalue()",
  "    ok = saida.strip() == EXPECTED.strip()",
  "except Exception:",
  "    saida = buf.getvalue()",
  "    erro = traceback.format_exc(limit=3)",
  "json.dumps({'ok': bool(ok), 'saida': saida, 'erro': erro})"
].join("\n");

async function run() {
  var btn = document.getElementById("run");
  var status = document.getElementById("status");
  btn.disabled = true;
  status.textContent = "Carregando sandbox (1ª vez baixa ~15 MB)...";
  try {
    var pyodide = await getPyodide();
    status.textContent = "Executando...";
    pyodide.globals.set("STUDENT_CODE", document.getElementById("code").value);
    pyodide.globals.set("EXPECTED", EXPECTED);
    var out = pyodide.runPython(RUNNER);
    render(JSON.parse(out));
  } catch (err) {
    status.textContent = "Erro ao carregar a sandbox: " + err;
  } finally {
    btn.disabled = false;
  }
}

function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function render(data) {
  document.getElementById("saida").textContent = data.saida ? data.saida : "(sem saída)";
  var status = document.getElementById("status");
  var erroDiv = document.getElementById("erro");
  if (data.erro) {
    erroDiv.innerHTML = "<pre class='fail'>" + esc(data.erro) + "</pre>";
  } else {
    erroDiv.innerHTML = "";
  }
  if (data.ok) {
    status.innerHTML = "<span class='ok'>🎉 Saída correta!</span>";
  } else {
    status.innerHTML = "<span class='fail'>A saída ainda não bate com o esperado.</span>";
  }
}

document.getElementById("run").onclick = run;
</script>
</body>
</html>
""")


def exercicio_saida_sandbox(chave, enunciado, esperado, modelo="",
                            dica="", pyodide_version="0.29.4", height=560):
    """
    Tarefa Rodar/Modificar em sandbox Pyodide: roda o PROGRAMA do aluno no
    navegador, captura o stdout e compara com `esperado` (ignorando espaços nas
    pontas). Sem comprovante — estas fases não entregam nada.

    Substituto direto do `componentes.exercicio_saida`, sem o parâmetro
    `stdin_text` (nenhuma página usa entrada padrão).
    """
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)
    html = _HTML_SAIDA.safe_substitute(
        MODELO=modelo,
        ESPERADO=json.dumps(esperado),
        PYVER=pyodide_version,
    )
    components.html(html, height=height, scrolling=True)
```

- [ ] **Step 4: Verificar compilação e os testes**

Run: `/usr/local/bin/python3.11 -m py_compile utils/sandbox_pyodide.py && /usr/local/bin/python3.11 tests/test_saida_sandbox.py`
Expected: compila sem erro; testes PASS.

- [ ] **Step 5: Commit**

```bash
git add utils/sandbox_pyodide.py tests/test_saida_sandbox.py
git commit -m "feat(sandbox): exercicio_saida_sandbox (Rodar/Modificar via Pyodide)"
```

---

### Task 3: Migrar as 32 páginas (import + chamada)

Troca mecânica e idêntica em todas: `from utils.componentes import exercicio_saida` → `from utils.sandbox_pyodide import exercicio_saida_sandbox`, e `exercicio_saida(` → `exercicio_saida_sandbox(`. Como nenhuma página usa `stdin_text`, a assinatura é compatível.

**Files:**
- Modify: `pages/*/02_rodar.py` e `pages/*/04_modificar.py` (32 arquivos)

- [ ] **Step 1: Confirmar que cada página importa SÓ `exercicio_saida` de componentes**

Run:
```bash
grep -rL "from utils.componentes import exercicio_saida$" $(grep -rl "exercicio_saida(" pages)
```
Expected: vazio (toda página com `exercicio_saida(` tem exatamente esse import). Se aparecer algum arquivo, ele importa algo a mais de `componentes` — trate manualmente antes do script.

- [ ] **Step 2: Rodar o script de migração**

Run:
```bash
/usr/local/bin/python3.11 - <<'PY'
from pathlib import Path
imp_old = "from utils.componentes import exercicio_saida"
imp_new = "from utils.sandbox_pyodide import exercicio_saida_sandbox"
n = 0
for f in list(Path("pages").glob("*/02_rodar.py")) + list(Path("pages").glob("*/04_modificar.py")):
    txt = f.read_text()
    if "exercicio_saida(" not in txt:
        continue
    txt = txt.replace(imp_old, imp_new)
    txt = txt.replace("exercicio_saida(", "exercicio_saida_sandbox(")
    f.write_text(txt)
    n += 1
print(f"{n} páginas migradas")
PY
```
Expected: `32 páginas migradas`.

- [ ] **Step 3: Verificar que não sobrou `exercicio_saida` server-side nas páginas**

Run:
```bash
grep -rn "exercicio_saida\b" pages | grep -v "exercicio_saida_sandbox" || echo "(nenhum resíduo)"
grep -rln "from utils.componentes import" pages || echo "(nenhuma página usa componentes)"
```
Expected: `(nenhum resíduo)` e `(nenhuma página usa componentes)`.

- [ ] **Step 4: Compilar tudo e rodar a suíte**

Run:
```bash
/usr/local/bin/python3.11 -m py_compile pages/*/*.py && \
for t in tests/test_*.py; do /usr/local/bin/python3.11 "$t" >/dev/null 2>&1 && echo "✅ $(basename $t)" || echo "❌ $(basename $t)"; done
```
Expected: compila OK; todos os testes ✅ (incluindo `test_saida_sandbox.py`, que agora valida as chamadas já como `exercicio_saida_sandbox`).

- [ ] **Step 5: Commit**

```bash
git add pages/
git commit -m "refactor(rodar/modificar): roda no Pyodide (navegador), não no servidor"
```

---

### Task 4: Verificação manual no navegador (Pyodide)

O comportamento JS/Pyodide não dá para testar em CI sem navegador headless; confirme à mão.

**Files:** nenhum (verificação)

- [ ] **Step 1: Subir o app**

Run: `/usr/local/bin/python3.11 -m streamlit run streamlit_app.py`
(ou peça ao usuário rodar `! streamlit run streamlit_app.py`)

- [ ] **Step 2: Testar uma fase Rodar**

Abra **Tema 5 · Repetição → Rodar**. Clique **Rodar e verificar (sandbox)**.
Expected: aparece a saída `60` e o status verde "🎉 Saída correta!". Na contagem regressiva, `5 4 3 2 1 Fim!`.

- [ ] **Step 3: Testar uma fase Modificar (estado quebrado e corrigido)**

Abra **Tema 8 · Matrizes → Modificar**. Rode sem mexer.
Expected: saída `0` e status vermelho. Troque `tabuleiro[coluna][linha]` por `tabuleiro[linha][coluna]`, rode de novo.
Expected: saída `1` e status verde.

- [ ] **Step 4: Confirmar que o servidor não executou nada**

Observe que a 1ª execução baixa o runtime do Pyodide (~15 MB) no navegador — sinal de que roda no cliente. (Opcional: confirme que `utils/autograder.py` não foi chamado, ex.: sem logs de execução no terminal do Streamlit.)

---

### Task 5: Atualizar a documentação

**Files:**
- Modify: `README.md` (seção "⚠️ Segurança do autograder")

- [ ] **Step 1: Atualizar a seção de segurança do README**

Substitua o parágrafo da seção "## ⚠️ Segurança do autograder" por:

```markdown
## ⚠️ Segurança do autograder

**Todas as fases que executam código do aluno (Rodar, Modificar e Criar) rodam no
navegador, via Pyodide (CPython em WebAssembly).** Nada de código de aluno roda no
servidor — bom para publicar o app aberto e para escalar (um laço infinito trava
só a aba do próprio aluno, não o servidor).

`utils/autograder.py` (server-side, com `exec` e builtins restritos) **não está
mais no caminho de execução** das páginas; permanece apenas para os testes
automatizados e como utilitário opcional. Se for reusá-lo para execução real,
lembre que os builtins restritos **não** são uma sandbox segura — prefira o
Pyodide.
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: Rodar/Modificar/Criar rodam no navegador (Pyodide)"
```

---

## Self-Review

**1. Spec coverage**
- Mover Rodar/Modificar para Pyodide → Tasks 2 (helper) + 3 (migração das 32 páginas). ✅
- Remover risco de laço infinito no servidor → consequência da Task 3 (nada roda no servidor); documentado na Task 5. ✅
- Sem comprovante em Rodar/Modificar → helper da Task 2 não tem UI de entrega. ✅
- Sem regressão de conteúdo → Task 1 (guarda AST) + Task 3 Step 4 (suíte). ✅
- `stdin` não usado → confirmado no contexto; helper omite `stdin_text`. ✅

**2. Placeholder scan:** sem "TBD/TODO/etc."; todo código (helper, template, testes, scripts) está completo. ✅

**3. Type/identidade consistente:** o nome `exercicio_saida_sandbox` e a assinatura `(chave, enunciado, esperado, modelo, dica, pyodide_version, height)` são os mesmos na definição (Task 2), na migração (Task 3) e no teste que reconhece os dois nomes (Task 1). Globais JS `STUDENT_CODE`/`EXPECTED` batem entre o RUNNER e os `pyodide.globals.set(...)`. ✅

**Riscos conhecidos:**
- A Task 1 pode revelar um Modificar cujo modelo já produz o esperado (conteúdo mal-formado pré-existente) — é desejável que falhe e seja corrigido antes de migrar.
- Laço infinito no Pyodide congela a aba do aluno (não o servidor). Aceitável; melhoria futura opcional: usar o *interrupt buffer* do Pyodide para um botão "parar".
```
