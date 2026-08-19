import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    "Este **pipe** deveria aplicar as funções **na ordem em que aparecem**: "
    "começar em `3`, somar 1 (→ 4) e depois dobrar (→ **8**). Mas alguém aplicou "
    "os passos **na ordem errada** e a saída saiu como `7`. Conserte o `pipe` "
    "para a saída ser `8`."
)

exercicio_saida_sandbox(
    chave="t14_modificar",
    enunciado="Conserte o `pipe` para imprimir `8`:",
    esperado="8",
    modelo=(
        "def pipe(valor, *funcs):\n"
        "    for f in reversed(funcs):   # <- a ordem está invertida\n"
        "        valor = f(valor)\n"
        "    return valor\n"
        "\n"
        "print(pipe(3, lambda x: x + 1, lambda x: x * 2))"
    ),
    dica="O pipe deve percorrer `funcs` na ordem natural. Troque `reversed(funcs)` por apenas `funcs`.",
)

st.divider()
st.markdown(
    "💡 **O que observar:** com `reversed`, o `3` era dobrado primeiro (→ 6) e só "
    "depois somava 1 (→ 7). A composição depende da **ordem**: primeiro `+1`, "
    "depois `*2`, dá `(3+1)*2 = 8`."
)

rodape_fases(__file__)
