import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia cada trecho **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''numeros = [1, 2, 3, 4]
print(list(map(lambda n: n + 1, numeros)))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "[2, 3, 4, 5]",
        "[1, 2, 3, 4]",
        "[1, 2, 3, 4, 5]",
        "10",
    ],
    0,
    success="Isso! `map` aplica `n + 1` a cada item: 1→2, 2→3, 3→4, 4→5.",
    error="`map(f, dados)` transforma cada item por `f`. Aqui soma 1 a cada um → `[2, 3, 4, 5]`.",
)

st.divider()

st.code(
    '''numeros = [1, 2, 3, 4, 5]
print(list(filter(lambda n: n > 2, numeros)))''',
    language="python",
)

stb.single_choice(
    "E aqui, com `filter`?",
    [
        "[3, 4, 5]",
        "[1, 2]",
        "[True, True, True]",
        "[1, 2, 3, 4, 5]",
    ],
    0,
    success="Exato! `filter` mantém só os itens em que a condição é verdadeira: 3, 4, 5.",
    error="`filter(f, dados)` mantém os itens em que `f` é verdadeiro — aqui, os maiores que 2.",
)

st.divider()

st.code(
    '''from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))''',
    language="python",
)

stb.single_choice(
    "Quanto imprime?",
    [
        "10",
        "[1, 2, 3, 4]",
        "4",
        "24",
    ],
    0,
    success="Isso! `reduce` soma dois a dois: ((1+2)+3)+4 = 10.",
    error="`reduce` combina os itens acumulando: ((1+2)+3)+4 = 10.",
)

rodape_fases(__file__)
