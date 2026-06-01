import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''c = 20
f = c * 9 / 5 + 32
print(f)''',
    language="python",
)

stb.true_or_false(
    "Este programa vai imprimir `68.0` (com casa decimal), e não `68`.",
    True,
    success="Isso! A divisão `/` sempre produz um `float`, então o resultado sai como `68.0`.",
    error="Releia: em Python, `9 / 5` usa divisão real (`/`), que devolve um número com casas decimais (`float`).",
)

st.divider()

st.code(
    '''a = 7
b = 2
print(a / b)
print(a // b)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "3.5\\n3",
        "3\\n3.5",
        "3.5\\n3.5",
        "3\\n3",
    ],
    0,
    success="Exato! `/` é divisão real (`3.5`); `//` é divisão inteira, que descarta a parte decimal (`3`).",
    error="Lembre: `/` devolve float (3.5); `//` arredonda para baixo e devolve inteiro (3).",
)

st.divider()

st.code(
    '''print(2 + 3 * 4)
print(10 % 3)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "14\\n1",
        "20\\n1",
        "14\\n0",
        "20\\n0",
    ],
    0,
    success="Isso! `*` vem antes de `+`, então `2 + 3*4 = 14`. E `10 % 3` é o **resto** da divisão de 10 por 3: `1`.",
    error="Precedência: `3*4` primeiro, depois `2 + 12 = 14`. E `%` dá o resto: `10 % 3 = 1`.",
)

rodape_fases(__file__)
