import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox

st.subheader("Fase 5 — 🛠️ Criar (entrega)")
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `media_notas(linhas)` que
recebe uma **lista de textos** (as linhas já lidas do arquivo) e **devolva**
(com `return`) a **média** das notas válidas.

Regras:
- use `try/except` para **ignorar** linhas que não são número (ex.: `"falta"`);
- se **não houver** nenhuma nota válida, devolva `0`.

> Aqui a lista chega pronta para você focar no tratamento de erro. Num programa
> completo, essas linhas viriam de `with open(...)` — a lógica de validação é a
> mesma.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t8_criar",
    enunciado="Implemente a função `media_notas`:",
    func_name="media_notas",
    cases=[
        ((["7", "8", "9"],), 8.0),
        ((["7", "x", "9"],), 8.0),
        (([],), 0),
        ((["10", "abc", "ab"],), 10.0),
        ((["5.0", "5"],), 5.0),
    ],
    modelo=(
        "def media_notas(linhas):\n"
        "    soma = 0\n"
        "    quantidade = 0\n"
        "    for linha in linhas:\n"
        "        # tente converter; ignore se nao der\n"
        "        pass\n"
        "    if quantidade == 0:\n"
        "        return 0\n"
        "    return soma / quantidade"
    ),
    dica="Dentro do `for`, use `try: nota = float(linha)` e, se der certo, some em `soma` e some 1 em `quantidade`. No `except ValueError: pass`.",
    nome_tarefa="tema8_media_notas",
)
