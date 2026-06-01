import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

print(fatorial(3))''',
    language="python",
)

stb.single_choice(
    "O que este programa imprime?",
    [
        "6",
        "3",
        "9",
        "0",
    ],
    0,
    success="Isso! `fatorial(3)` = 3 × `fatorial(2)` = 3 × 2 × `fatorial(1)` = 3 × 2 × 1 × `fatorial(0)` = 3 × 2 × 1 × 1 = 6.",
    error="Desça até o caso base: `fatorial(3)` = 3 × 2 × 1 × `fatorial(0)` (=1) = 6.",
)

st.divider()

st.code(
    '''def contagem(n):
    if n == 0:
        return
    print(n)
    contagem(n - 1)

contagem(3)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "3\\n2\\n1",
        "1\\n2\\n3",
        "3\\n2\\n1\\n0",
        "Nada — entra em loop infinito.",
    ],
    0,
    success="Exato! Imprime 3, depois chama `contagem(2)` (imprime 2), depois 1, e em `contagem(0)` o caso base para — sem imprimir o 0.",
    error="Cada chamada imprime `n` e chama `contagem(n-1)`: 3, 2, 1. Em `n == 0` o `return` para antes do print.",
)

st.divider()

st.code(
    '''def soma_lista(numeros):
    if numeros == []:
        return 0
    return numeros[0] + soma_lista(numeros[1:])

print(soma_lista([10, 20, 30]))''',
    language="python",
)

stb.single_choice(
    "O que este programa imprime?",
    [
        "60",
        "30",
        "10",
        "0",
    ],
    0,
    success="Isso! `10 + soma_lista([20, 30])` = `10 + 20 + soma_lista([30])` = `10 + 20 + 30 + soma_lista([])` (=0) = 60.",
    error="A recursão soma o primeiro item com a soma do resto: `10 + 20 + 30 = 60`. A lista vazia é o caso base (0).",
)

rodape_fases(__file__)
