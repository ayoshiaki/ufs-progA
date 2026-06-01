# Programação A — livro interativo

Curso introdutório de programação em Python baseado em **problemas com
dificuldade crescente**, do pensamento computacional até orientação a objetos.
Construído com [`streamlit_book`](https://streamlit-book.readthedocs.io).

## Como rodar

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Abre no navegador. O menu lateral lista os 13 temas; dentro de cada tema, os
botões **‹ ›** no topo navegam entre as fases.

## O método: 5 fases por tema (PRIMM)

Cada tema é resolvido em fases curtas de dificuldade crescente:

| Fase | Nome | O que o aluno faz | Ferramenta |
|------|------|-------------------|------------|
| 0 | Aquecimento | conhece o problema do tema | markdown |
| 1 | 🔮 Prever | lê código e prevê a saída | `stb.true_or_false`, `stb.single_choice` |
| 2 | ▶️ Rodar | executa e confirma | `exercicio_saida` |
| 3 | 🔍 Investigar | responde *por quê* | `stb.multiple_choice` |
| 4 | 🔧 Modificar | altera o código dado | `exercicio_saida` |
| 5 | 🛠️ Criar | resolve do zero — **entrega** | `exercicio_funcao` + `comprovante` |

As fases 1–4 são de autocorreção. A fase 5 gera um **comprovante de entrega**
baixável (com nome, matrícula, carimbo de tempo e hash).

## Plano de temas

1. **Pensamento computacional** — entrada/processamento/saída, variáveis, pilares ✅ *completo*
2. **Tipos e expressões** — int/float/str/bool, operadores, precedência ✅ *completo*
3. **Expressões booleanas** — comparações, `and`/`or`/`not` ✅ *completo*
4. **Condicionais** — `if/elif/else` ✅ *completo*
5. **Repetição** — `for`, `while`, acumuladores ✅ *completo*
6. **Listas, tuplas e dicionários** ✅ *completo*
7. **Strings** — fatiamento, métodos, f-strings ✅ *completo*
8. **Funções** ✅ *completo*
9. **Recursão** — caso base, caso recursivo (fatorial, soma) ✅ *completo*
10. **Funções de ordem superior** — função como argumento, `lambda` ✅ *completo*
11. **Arquivos e tratamento de erros** ✅ *completo*
12. **Introdução a objetos** — classes, atributos, métodos ✅ *completo*
13. **OO: herança e polimorfismo** ✅ *completo*

Todos os 13 temas estão completos, cada um com as 5 fases PRIMM. As fases
"Criar" (entrega) rodam na sandbox Pyodide (WebAssembly, client-side).

> **Nota sobre o Tema 11 (Arquivos e erros):** a tarefa de entrega é
> `media_notas(linhas)` — recebe a lista de linhas já lidas (não um caminho de
> arquivo), porque a sandbox do navegador não tem acesso ao sistema de arquivos
> do servidor. As fases 0–4 ainda ensinam `with open(...)` e `try/except`.

## Como criar (ou reposicionar) um tema

A estrutura é convenção sobre configuração: a **pasta** `pages/NN_nome/` define o
tema (o prefixo `NN` é a ordem) e o prefixo de cada arquivo (`00_`…`05_`) define a
fase. Para um tema novo:

1. Copie uma pasta existente (ex.: `pages/01_pensamento_computacional/`) para
   `pages/NN_nome/`, na **posição didática** certa — se inserir no meio, renumere
   as pastas seguintes com `git mv` (e atualize os identificadores `chave`/
   `nome_tarefa` dentro delas).
2. Edite as 6 fases. Componentes prontos:
   - `exercicio_saida(chave, enunciado, esperado, modelo, stdin_text, dica)` —
     compara a saída (stdout). Usado nas fases Rodar/Modificar.
   - `exercicio_funcao_sandbox(...)` / `exercicio_expressoes_sandbox(...)` em
     `utils/sandbox_pyodide.py` — testam função/expressão na sandbox. Fase Criar.
3. Registre o tema nas **duas fontes-espelho** (precisam concordar):
   `streamlit_app.py` (`options`/`paths`/`icons`) e `utils/navegacao.py` (`TEMAS`).
4. Rode `python tests/test_estrutura_temas.py` — ele garante que pastas, `TEMAS` e
   as listas de `streamlit_app.py` batem (numeração contígua 1..N).

## Coletando as entregas

O comprovante é um `.txt` baixável. Algumas formas de receber:

- **Mais simples:** aluno baixa o `.txt` e anexa num formulário (Google Forms) ou no Moodle/SIGAA.
- **GitHub Classroom:** aluno faz commit do código + comprovante.
- **Correção em lote:** os arquivos de entrega podem ser corrigidos depois com
  seu fluxo de correção habitual.

> `save_answers=True` (em `streamlit_app.py`) também registra as respostas dos
> quizzes; veja a *Admin View* do `streamlit_book` para estatísticas.

## ⚠️ Segurança do autograder

`utils/autograder.py` usa `exec` para rodar o código do aluno. Para uso local ou
com turma confiável, tudo bem. **Se for publicar o app aberto na internet**,
substitua por uma sandbox real (Pyodide no navegador, Judge0, subprocess com
limites de tempo/memória). Os builtins estão restritos, mas isso *não* é uma
sandbox segura.

> Para suportar OO (Temas 12–13), a whitelist libera `__build_class__`, `object`,
> `super` etc. — necessário para definir classes, mas `object` é um vetor
> clássico de escape. Reforça a recomendação: deploy aberto → porte as fases
> Rodar/Modificar para Pyodide (as fases Criar de OO já usam Pyodide).

## Estrutura

```
programacao-a/
├── streamlit_app.py          # configura o livro e os capítulos
├── requirements.txt
├── README.md
├── utils/
│   ├── autograder.py         # executa e testa código do aluno
│   ├── componentes.py        # caixas de exercício + comprovante
│   ├── navegacao.py          # bússola: tema/fase derivados do caminho
│   ├── progresso.py          # cartão "Salvar progresso" na sidebar
│   └── sandbox_pyodide.py    # sandbox WebAssembly (fases "Criar")
└── pages/
    ├── 00_boas_vindas.py
    ├── 01_pensamento_computacional/   # cada tema é uma pasta NN_nome/
    │   ├── 00_intro.py … 05_criar.py  #   com as 6 fases PRIMM
    └── 02_tipos/ … 13_heranca/        # 13 temas, todos completos
```

## Sandbox real para o autograder

O `utils/autograder.py` (baseado em `exec`) é só para uso local/confiável. Para
execução isolada de verdade, há dois caminhos prontos:

### Opção A — Pyodide (recomendada, grátis, client-side) — `utils/sandbox_pyodide.py`
O código do aluno roda no **navegador dele**, compilado para WebAssembly. Nada é
executado no servidor → seguro para o Streamlit Community Cloud, sem custo de CPU.
Já está ligado em **todas** as fases "Criar":

```python
from utils.sandbox_pyodide import exercicio_funcao_sandbox
exercicio_funcao_sandbox(chave="t1_criar", enunciado="...",
                         func_name="valor_total",
                         cases=[((5,3),15)], modelo="...", nome_tarefa="t1")
```

A 1ª execução baixa ~15 MB do runtime (fica em cache). **Atenção:** os casos de
teste viajam embutidos na página, então não ficam secretos.

Para tarefas que entregam uma **classe** (Temas 12 e 13), use
`exercicio_expressoes_sandbox(...)`, que avalia *expressões* em vez de só
`func(*args)`. Cada caso é um trecho que termina atribuindo o resultado a
`_res`:

```python
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
exercicio_expressoes_sandbox(chave="t12_criar", enunciado="...",
    cases=[("c = ContaBancaria(100); c.sacar(30); _res = c.saldo", 70)],
    modelo="class ContaBancaria:\n    ...", nome_tarefa="tema12")
```

### Opção B — Judge0 (server-side, esconde o gabarito) — `utils/sandbox_judge0.py`
O código roda em container isolado (sandbox Isolate) no servidor; os casos de
teste ficam no servidor, invisíveis ao aluno. Endpoint via **self-host Docker**
(grátis, ilimitado) ou **RapidAPI** (plano Basic grátis com cota). Configure em
`.streamlit/secrets.toml` (veja o cabeçalho do arquivo) e adicione `requests`.

### Resumo
| | exec (padrão) | Pyodide | Judge0 |
|---|---|---|---|
| Isolamento real | ❌ | ✅ (WASM) | ✅ (container) |
| Funciona no Community Cloud grátis | ✅ | ✅ | só via API externa |
| Custo de servidor | baixo | zero | self-host ou API |
| Esconde o gabarito | — | ❌ | ✅ |

> As fases "Rodar"/"Modificar" ainda usam `exercicio_saida` (exec no servidor).
> Para um deploy 100% sandboxed, porte-as para Pyodide seguindo o mesmo padrão.

## Ocultar o gabarito com Pyodide

Importante: **Pyodide puro não esconde o gabarito de forma robusta** — o que o
navegador precisa para checar a resposta fica acessível ao aluno via devtools.
Há duas abordagens:

### Casual — gabarito por hash (`utils/sandbox_hash.py`)
Só o SHA-256 de cada resposta vai à página; as respostas em claro nunca são
enviadas. Bom contra "ler a resposta no código-fonte". **Fraco** quando a saída
tem espaço pequeno (inteiros/booleanos), pois permite brute force — o salt
também está no cliente. Ideal para saídas de alta entropia (strings/estruturas).

```python
from utils.sandbox_hash import exercicio_funcao_hash
exercicio_funcao_hash(chave="t6_criar", enunciado="Implemente `inverter(texto)`:",
                      func_name="inverter",
                      cases=[(("python",), "nohtyp")],   # respostas só viram hash
                      modelo="def inverter(texto):\n    return texto",
                      salt="segredo-da-disciplina", nome_tarefa="t6_inverter")
```

### Robusto — Pyodide + endpoint de correção (recomendado p/ sigilo real)
O código roda no navegador (Pyodide); só a **comparação** vai a um endpoint
stateless que guarda o gabarito no servidor e responde apenas passou/não passou.
O gabarito nunca sai do servidor, e dá para aplicar rate-limit (mata o brute
force). Como o endpoint só compara JSON (não executa código), roda no tier
grátis do Cloud Run/Functions — sem container privilegiado, sem cgroup, sem
Judge0.

### Robusto — arquivos prontos (implementado)
- **Endpoint:** `grading_endpoint/` (`main.py`, `gabarito.py`, `requirements.txt`,
  `DEPLOY.md`). É uma Cloud Function que **não executa código** — só compara as
  saídas enviadas com o gabarito secreto, com rate-limit por matrícula e
  auditoria no Cloud Logging. Edite as respostas em `gabarito.py`.
- **Cliente:** `utils/grade_client.py` → `exercicio_funcao_remoto(...)`. Roda o
  código no navegador (Pyodide), envia só as saídas e recebe passou/não-passou.

```python
from utils.grade_client import exercicio_funcao_remoto
exercicio_funcao_remoto(
    chave="t1_criar", enunciado="Implemente `valor_total(preco, quantidade)`:",
    func_name="valor_total",
    args_publicos=[[5, 3], [10, 0], [2, 4]],   # entradas são públicas
    task_id="tema1_valor_total",               # respostas vivem no servidor
    modelo="def valor_total(preco, quantidade):\n    return 0",
)
```

Configure `GRADE_URL` e `CLASS_TOKEN` em `.streamlit/secrets.toml` (passos no
`grading_endpoint/DEPLOY.md`). As entradas (`args_publicos` no cliente) e as
respostas (`expected` no `gabarito.py`) devem ficar **na mesma ordem**.

### Hospedagem do corretor — grátis e sem cartão
O endpoint tem adaptadores prontos para hosts gratuitos **sem cartão de crédito**:
`app.py` (FastAPI → Hugging Face Spaces/Render) e `flask_app.py` (→ PythonAnywhere),
ambos reusando `grading_core.py`. Passo a passo em
`grading_endpoint/README_HOSPEDAGEM.md`. O Google Cloud Function (`main.py`)
continua disponível, mas exige conta de faturamento com cartão mesmo no free tier.

Stack 100% gratuita e sem cartão: **Streamlit Community Cloud** (app) +
**Pyodide/CDN** (execução) + **Hugging Face Spaces ou PythonAnywhere** (corretor).
