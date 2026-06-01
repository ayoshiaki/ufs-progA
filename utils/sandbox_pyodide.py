"""
Autograder com SANDBOX REAL via Pyodide (CPython compilado para WebAssembly).

O código do aluno NUNCA roda no servidor: ele é executado dentro do navegador,
isolado pela sandbox do WebAssembly. Isso é seguro para publicar no Streamlit
Community Cloud, é gratuito e não consome CPU do servidor.

Uso (substitui exercicio_funcao das fases "Criar"):

    from utils.sandbox_pyodide import exercicio_funcao_sandbox
    exercicio_funcao_sandbox(
        chave="t1_criar",
        enunciado="Implemente `valor_total(preco, quantidade)`:",
        func_name="valor_total",
        cases=[((5, 3), 15), ((10, 0), 0), ((2, 4), 8)],
        modelo="def valor_total(preco, quantidade):\\n    return 0",
        nome_tarefa="tema1_valor_total",
    )

Limitações honestas:
- Os casos de teste vão embutidos na página → um aluno avançado consegue lê-los
  no devtools. Se PRECISA esconder o gabarito, use Judge0 (sandbox_judge0.py).
- 1ª execução baixa ~15 MB do runtime (fica em cache depois).
- Só pacotes Python puros / disponíveis no Pyodide (numpy, pandas etc. existem).
"""

import json
from string import Template

import streamlit as st
import streamlit.components.v1 as components

_HTML = Template(r"""
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
  table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  th, td { border: 1px solid #e0e0e0; padding: 6px 8px; text-align: left; }
  th { background: #f5f5f5; }
  .ok { color: #137333; } .fail { color: #c5221f; }
  .status { margin-top: 10px; font-size: 14px; }
  .box { background: #f0fff4; border: 1px solid #a3e3b8; border-radius: 8px; padding: 12px; margin-top: 12px; }
  input { padding: 6px 8px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin: 4px 0; width: 60%; }
  code { background: #f0f0f0; padding: 1px 4px; border-radius: 4px; }
</style>
</head>
<body>
  <textarea id="code" rows="9">$MODELO</textarea>
  <div><button id="run">Rodar e verificar (sandbox)</button>
       <span class="status" id="status"></span></div>
  <div id="results"></div>
  <div id="entrega"></div>

<script src="https://cdn.jsdelivr.net/pyodide/v$PYVER/full/pyodide.js"></script>
<script>
var FUNC_NAME   = $FUNC_NAME;
var CASES_JSON  = $CASES_JSON;
var NOME_TAREFA = $NOME_TAREFA;
var pyodideReady = null;

function getPyodide() {
  if (!pyodideReady) { pyodideReady = loadPyodide(); }
  return pyodideReady;
}

var RUNNER = [
  "import json, traceback",
  "ns = {}",
  "results = []",
  "ok_all = True",
  "try:",
  "    exec(STUDENT_CODE, ns)",
  "    func = ns.get(FUNC_NAME)",
  "    if not callable(func):",
  "        ok_all = False",
  "        results.append({'args':'—','esperado':'—','obtido':'função `'+FUNC_NAME+'` não encontrada','ok':False})",
  "    else:",
  "        for case in json.loads(CASES_JSON):",
  "            args = case['args']; esperado = case['expected']",
  "            try:",
  "                obtido = func(*args)",
  "                ok = obtido == esperado",
  "            except Exception as e:",
  "                obtido = 'ERRO: ' + str(e); ok = False",
  "            ok_all = ok_all and bool(ok)",
  "            results.append({'args':repr(tuple(args)),'esperado':repr(esperado),'obtido':repr(obtido),'ok':bool(ok)})",
  "except Exception:",
  "    ok_all = False",
  "    results.append({'args':'—','esperado':'—','obtido':traceback.format_exc(limit=2),'ok':False})",
  "json.dumps({'ok_all': ok_all, 'results': results})"
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
    pyodide.globals.set("FUNC_NAME", FUNC_NAME);
    pyodide.globals.set("CASES_JSON", CASES_JSON);
    var out = pyodide.runPython(RUNNER);
    render(JSON.parse(out));
  } catch (err) {
    status.textContent = "Erro ao carregar a sandbox: " + err;
  } finally {
    btn.disabled = false;
  }
}

function render(data) {
  var status = document.getElementById("status");
  var rows = data.results.map(function (r) {
    var mark = r.ok ? "<span class='ok'>✅</span>" : "<span class='fail'>❌</span>";
    return "<tr><td>" + mark + "</td><td><code>" + esc(r.args) +
           "</code></td><td><code>" + esc(r.esperado) +
           "</code></td><td><code>" + esc(r.obtido) + "</code></td></tr>";
  }).join("");
  document.getElementById("results").innerHTML =
    "<table><tr><th></th><th>entrada</th><th>esperado</th><th>obtido</th></tr>" +
    rows + "</table>";
  if (data.ok_all) {
    status.innerHTML = "<span class='ok'>🎉 Todos os testes passaram!</span>";
    mostrarEntrega();
  } else {
    status.innerHTML = "<span class='fail'>Ainda não passou em todos os casos.</span>";
    document.getElementById("entrega").innerHTML = "";
  }
}

function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function mostrarEntrega() {
  document.getElementById("entrega").innerHTML =
    "<div class='box'><b>📤 Entrega</b><br>" +
    "Nome completo:<br><input id='nome'><br>" +
    "Matrícula:<br><input id='mat'><br>" +
    "<button id='dl'>📄 Baixar comprovante</button></div>";
  document.getElementById("dl").onclick = baixar;
}

async function sha12(s) {
  if (window.crypto && crypto.subtle) {
    var buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
    return Array.from(new Uint8Array(buf)).map(function(b){
      return b.toString(16).padStart(2, "0"); }).join("").slice(0, 12);
  }
  var h = 0; for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) | 0; }
  return (h >>> 0).toString(16);
}

async function baixar() {
  var nome = document.getElementById("nome").value.trim();
  var mat  = document.getElementById("mat").value.trim();
  if (!nome || !mat) { alert("Preencha nome e matrícula."); return; }
  var codigo = document.getElementById("code").value;
  var agora = new Date().toISOString().slice(0, 19).replace("T", " ");
  var assin = await sha12(mat + codigo + agora);
  var txt = "COMPROVANTE DE ENTREGA — Programação A\n" +
            "Tarefa: " + NOME_TAREFA + "\nAluno: " + nome + "\nMatrícula: " + mat +
            "\nData/hora: " + agora + "\nAssinatura: " + assin +
            "\n" + "-".repeat(50) + "\n" + codigo + "\n";
  var blob = new Blob([txt], { type: "text/plain" });
  var a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "entrega_" + NOME_TAREFA + "_" + mat + ".txt";
  a.click();
}

document.getElementById("run").onclick = run;
</script>
</body>
</html>
""")


def exercicio_funcao_sandbox(chave, enunciado, func_name, cases, modelo="",
                             dica="", nome_tarefa=None, pyodide_version="0.29.4",
                             height=640):
    """Tarefa de função corrigida em sandbox WebAssembly (client-side)."""
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)

    cases_payload = json.dumps(
        [{"args": list(args), "expected": expected} for args, expected in cases]
    )
    html = _HTML.safe_substitute(
        MODELO=modelo,                              # vai dentro de <textarea>: texto cru ok
        FUNC_NAME=json.dumps(func_name),            # vira string JS válida
        CASES_JSON=json.dumps(cases_payload),       # string JS contendo o JSON
        NOME_TAREFA=json.dumps(nome_tarefa or chave),
        PYVER=pyodide_version,
    )
    components.html(html, height=height, scrolling=True)


# ---------------------------------------------------------------------------
# Variante por EXPRESSÕES — para tarefas que entregam uma CLASSE (ou qualquer
# coisa que não dá para testar só com `func(*args)`). Cada caso é um trecho de
# código que termina atribuindo o resultado a `_res`; o esperado é comparado
# com `_res`. Ex.: ("c = ContaBancaria(100); c.sacar(30); _res = c.saldo", 70)
# ---------------------------------------------------------------------------

_HTML_EXPR = Template(r"""
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
  table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  th, td { border: 1px solid #e0e0e0; padding: 6px 8px; text-align: left; }
  th { background: #f5f5f5; }
  .ok { color: #137333; } .fail { color: #c5221f; }
  .status { margin-top: 10px; font-size: 14px; }
  .box { background: #f0fff4; border: 1px solid #a3e3b8; border-radius: 8px; padding: 12px; margin-top: 12px; }
  input { padding: 6px 8px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin: 4px 0; width: 60%; }
  code { background: #f0f0f0; padding: 1px 4px; border-radius: 4px; }
</style>
</head>
<body>
  <textarea id="code" rows="12">$MODELO</textarea>
  <div><button id="run">Rodar e verificar (sandbox)</button>
       <span class="status" id="status"></span></div>
  <div id="results"></div>
  <div id="entrega"></div>

<script src="https://cdn.jsdelivr.net/pyodide/v$PYVER/full/pyodide.js"></script>
<script>
var CASES_JSON  = $CASES_JSON;
var NOME_TAREFA = $NOME_TAREFA;
var pyodideReady = null;

function getPyodide() {
  if (!pyodideReady) { pyodideReady = loadPyodide(); }
  return pyodideReady;
}

var RUNNER = [
  "import json, traceback",
  "results = []",
  "ok_all = True",
  "try:",
  "    base = {}",
  "    exec(STUDENT_CODE, base)",
  "    for case in json.loads(CASES_JSON):",
  "        trecho = case['expr']; esperado = case['expected']",
  "        local = dict(base)",
  "        try:",
  "            exec(trecho, local)",
  "            obtido = local.get('_res')",
  "            ok = obtido == esperado",
  "        except Exception as e:",
  "            obtido = 'ERRO: ' + str(e); ok = False",
  "        ok_all = ok_all and bool(ok)",
  "        results.append({'args':trecho,'esperado':repr(esperado),'obtido':repr(obtido),'ok':bool(ok)})",
  "except Exception:",
  "    ok_all = False",
  "    results.append({'args':'—','esperado':'—','obtido':traceback.format_exc(limit=2),'ok':False})",
  "json.dumps({'ok_all': ok_all, 'results': results})"
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
    pyodide.globals.set("CASES_JSON", CASES_JSON);
    var out = pyodide.runPython(RUNNER);
    render(JSON.parse(out));
  } catch (err) {
    status.textContent = "Erro ao carregar a sandbox: " + err;
  } finally {
    btn.disabled = false;
  }
}

function render(data) {
  var status = document.getElementById("status");
  var rows = data.results.map(function (r) {
    var mark = r.ok ? "<span class='ok'>✅</span>" : "<span class='fail'>❌</span>";
    return "<tr><td>" + mark + "</td><td><code>" + esc(r.args) +
           "</code></td><td><code>" + esc(r.esperado) +
           "</code></td><td><code>" + esc(r.obtido) + "</code></td></tr>";
  }).join("");
  document.getElementById("results").innerHTML =
    "<table><tr><th></th><th>teste</th><th>esperado</th><th>obtido</th></tr>" +
    rows + "</table>";
  if (data.ok_all) {
    status.innerHTML = "<span class='ok'>🎉 Todos os testes passaram!</span>";
    mostrarEntrega();
  } else {
    status.innerHTML = "<span class='fail'>Ainda não passou em todos os casos.</span>";
    document.getElementById("entrega").innerHTML = "";
  }
}

function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function mostrarEntrega() {
  document.getElementById("entrega").innerHTML =
    "<div class='box'><b>📤 Entrega</b><br>" +
    "Nome completo:<br><input id='nome'><br>" +
    "Matrícula:<br><input id='mat'><br>" +
    "<button id='dl'>📄 Baixar comprovante</button></div>";
  document.getElementById("dl").onclick = baixar;
}

async function sha12(s) {
  if (window.crypto && crypto.subtle) {
    var buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
    return Array.from(new Uint8Array(buf)).map(function(b){
      return b.toString(16).padStart(2, "0"); }).join("").slice(0, 12);
  }
  var h = 0; for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) | 0; }
  return (h >>> 0).toString(16);
}

async function baixar() {
  var nome = document.getElementById("nome").value.trim();
  var mat  = document.getElementById("mat").value.trim();
  if (!nome || !mat) { alert("Preencha nome e matrícula."); return; }
  var codigo = document.getElementById("code").value;
  var agora = new Date().toISOString().slice(0, 19).replace("T", " ");
  var assin = await sha12(mat + codigo + agora);
  var txt = "COMPROVANTE DE ENTREGA — Programação A\n" +
            "Tarefa: " + NOME_TAREFA + "\nAluno: " + nome + "\nMatrícula: " + mat +
            "\nData/hora: " + agora + "\nAssinatura: " + assin +
            "\n" + "-".repeat(50) + "\n" + codigo + "\n";
  var blob = new Blob([txt], { type: "text/plain" });
  var a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "entrega_" + NOME_TAREFA + "_" + mat + ".txt";
  a.click();
}

document.getElementById("run").onclick = run;
</script>
</body>
</html>
""")


def exercicio_expressoes_sandbox(chave, enunciado, cases, modelo="",
                                 dica="", nome_tarefa=None,
                                 pyodide_version="0.29.4", height=700):
    """
    Tarefa corrigida em sandbox WebAssembly por EXPRESSÕES — ideal para classes.

    cases: lista de (trecho, esperado), onde `trecho` é um código que termina
        atribuindo o resultado a `_res`. Cada caso roda num namespace novo
        derivado do código do aluno.
        ex: [("c = ContaBancaria(100); c.sacar(30); _res = c.saldo", 70)]
    """
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)

    cases_payload = json.dumps(
        [{"expr": expr, "expected": expected} for expr, expected in cases]
    )
    html = _HTML_EXPR.safe_substitute(
        MODELO=modelo,
        CASES_JSON=json.dumps(cases_payload),
        NOME_TAREFA=json.dumps(nome_tarefa or chave),
        PYVER=pyodide_version,
    )
    components.html(html, height=height, scrolling=True)


# ---------------------------------------------------------------------------
# Variante por SCRIPT — para temas ANTES de Funções. O aluno NÃO escreve `def`:
# escreve um script que usa variáveis de entrada já existentes e guarda o
# resultado em `_res`. O script roda UMA VEZ POR CASO, com entradas diferentes
# injetadas antes — mantendo o rigor de múltiplos casos (anti-chute) sem função.
# Ex.: casos=[({"preco": 5, "quantidade": 3}, 15)] e o aluno escreve
#      `_res = preco * quantidade`.
# ---------------------------------------------------------------------------

_HTML_SCRIPT = Template(r"""
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
  table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  th, td { border: 1px solid #e0e0e0; padding: 6px 8px; text-align: left; }
  th { background: #f5f5f5; }
  .ok { color: #137333; } .fail { color: #c5221f; }
  .status { margin-top: 10px; font-size: 14px; }
  .box { background: #f0fff4; border: 1px solid #a3e3b8; border-radius: 8px; padding: 12px; margin-top: 12px; }
  input { padding: 6px 8px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin: 4px 0; width: 60%; }
  code { background: #f0f0f0; padding: 1px 4px; border-radius: 4px; }
</style>
</head>
<body>
  <textarea id="code" rows="12">$MODELO</textarea>
  <div><button id="run">Rodar e verificar (sandbox)</button>
       <span class="status" id="status"></span></div>
  <div id="results"></div>
  <div id="entrega"></div>

<script src="https://cdn.jsdelivr.net/pyodide/v$PYVER/full/pyodide.js"></script>
<script>
var CASES_JSON  = $CASES_JSON;
var NOME_TAREFA = $NOME_TAREFA;
var pyodideReady = null;

function getPyodide() {
  if (!pyodideReady) { pyodideReady = loadPyodide(); }
  return pyodideReady;
}

var RUNNER = [
  "import json, traceback",
  "results = []",
  "ok_all = True",
  "try:",
  "    for case in json.loads(CASES_JSON):",
  "        entradas = case['inputs']; esperado = case['expected']",
  "        ns = dict(entradas)",
  "        try:",
  "            exec(STUDENT_CODE, ns)",
  "            obtido = ns.get('_res')",
  "            ok = obtido == esperado",
  "        except Exception as e:",
  "            obtido = 'ERRO: ' + str(e); ok = False",
  "        ok_all = ok_all and bool(ok)",
  "        entrada_txt = ', '.join(k + '=' + repr(v) for k, v in entradas.items())",
  "        results.append({'args':entrada_txt,'esperado':repr(esperado),'obtido':repr(obtido),'ok':bool(ok)})",
  "except Exception:",
  "    ok_all = False",
  "    results.append({'args':'—','esperado':'—','obtido':traceback.format_exc(limit=2),'ok':False})",
  "json.dumps({'ok_all': ok_all, 'results': results})"
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
    pyodide.globals.set("CASES_JSON", CASES_JSON);
    var out = pyodide.runPython(RUNNER);
    render(JSON.parse(out));
  } catch (err) {
    status.textContent = "Erro ao carregar a sandbox: " + err;
  } finally {
    btn.disabled = false;
  }
}

function render(data) {
  var status = document.getElementById("status");
  var rows = data.results.map(function (r) {
    var mark = r.ok ? "<span class='ok'>✅</span>" : "<span class='fail'>❌</span>";
    return "<tr><td>" + mark + "</td><td><code>" + esc(r.args) +
           "</code></td><td><code>" + esc(r.esperado) +
           "</code></td><td><code>" + esc(r.obtido) + "</code></td></tr>";
  }).join("");
  document.getElementById("results").innerHTML =
    "<table><tr><th></th><th>entrada</th><th>esperado</th><th>obtido (_res)</th></tr>" +
    rows + "</table>";
  if (data.ok_all) {
    status.innerHTML = "<span class='ok'>🎉 Todos os testes passaram!</span>";
    mostrarEntrega();
  } else {
    status.innerHTML = "<span class='fail'>Ainda não passou em todos os casos.</span>";
    document.getElementById("entrega").innerHTML = "";
  }
}

function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function mostrarEntrega() {
  document.getElementById("entrega").innerHTML =
    "<div class='box'><b>📤 Entrega</b><br>" +
    "Nome completo:<br><input id='nome'><br>" +
    "Matrícula:<br><input id='mat'><br>" +
    "<button id='dl'>📄 Baixar comprovante</button></div>";
  document.getElementById("dl").onclick = baixar;
}

async function sha12(s) {
  if (window.crypto && crypto.subtle) {
    var buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
    return Array.from(new Uint8Array(buf)).map(function(b){
      return b.toString(16).padStart(2, "0"); }).join("").slice(0, 12);
  }
  var h = 0; for (var i = 0; i < s.length; i++) { h = (h * 31 + s.charCodeAt(i)) | 0; }
  return (h >>> 0).toString(16);
}

async function baixar() {
  var nome = document.getElementById("nome").value.trim();
  var mat  = document.getElementById("mat").value.trim();
  if (!nome || !mat) { alert("Preencha nome e matrícula."); return; }
  var codigo = document.getElementById("code").value;
  var agora = new Date().toISOString().slice(0, 19).replace("T", " ");
  var assin = await sha12(mat + codigo + agora);
  var txt = "COMPROVANTE DE ENTREGA — Programação A\n" +
            "Tarefa: " + NOME_TAREFA + "\nAluno: " + nome + "\nMatrícula: " + mat +
            "\nData/hora: " + agora + "\nAssinatura: " + assin +
            "\n" + "-".repeat(50) + "\n" + codigo + "\n";
  var blob = new Blob([txt], { type: "text/plain" });
  var a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "entrega_" + NOME_TAREFA + "_" + mat + ".txt";
  a.click();
}

document.getElementById("run").onclick = run;
</script>
</body>
</html>
""")


def exercicio_script_sandbox(chave, enunciado, casos, modelo="",
                             dica="", nome_tarefa=None,
                             pyodide_version="0.29.4", height=720):
    """
    Tarefa em sandbox para temas ANTES de Funções: o aluno escreve um SCRIPT
    (sem `def`) que usa variáveis de entrada já existentes e guarda o resultado
    em `_res`. O script roda uma vez por caso, com entradas diferentes injetadas
    antes de executar — mantendo o rigor de múltiplos casos sem exigir função.

    casos: lista de (entradas, esperado), onde `entradas` é um dict
        nome_da_variavel -> valor, injetado antes de rodar o código do aluno.
        ex: [({"preco": 5, "quantidade": 3}, 15), ({"preco": 2, "quantidade": 4}, 8)]
    """
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)

    cases_payload = json.dumps(
        [{"inputs": entradas, "expected": esperado} for entradas, esperado in casos]
    )
    html = _HTML_SCRIPT.safe_substitute(
        MODELO=modelo,
        CASES_JSON=json.dumps(cases_payload),
        NOME_TAREFA=json.dumps(nome_tarefa or chave),
        PYVER=pyodide_version,
    )
    components.html(html, height=height, scrolling=True)
