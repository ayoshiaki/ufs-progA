import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia cada trecho **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''quadrados = [n * n for n in range(1, 5)]
print(quadrados)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "[1, 4, 9, 16]",
        "[1, 2, 3, 4]",
        "[2, 4, 6, 8]",
        "16",
    ],
    0,
    success="Isso! `range(1, 5)` dá 1, 2, 3, 4; cada um ao quadrado vira 1, 4, 9, 16.",
    error="A compreensão calcula `n * n` para cada `n` em 1, 2, 3, 4 → `[1, 4, 9, 16]`.",
)

st.divider()

st.code(
    '''pares = [n for n in range(1, 7) if n % 2 == 0]
print(pares)''',
    language="python",
)

stb.single_choice(
    "E aqui, com o filtro `if`?",
    [
        "[2, 4, 6]",
        "[1, 3, 5]",
        "[2, 4, 6, 8]",
        "[1, 2, 3, 4, 5, 6]",
    ],
    0,
    success="Exato! O `if n % 2 == 0` deixa passar só os pares: 2, 4, 6.",
    error="O filtro mantém apenas os itens em que a condição é verdadeira — os pares 2, 4, 6.",
)

st.divider()

st.code(
    '''numeros = [1, 2, 2, 3, 3, 3]
unicos = {n for n in numeros}
print(len(unicos))''',
    language="python",
)

stb.single_choice(
    "Quanto imprime? (repare nas chaves `{}` — é um conjunto)",
    [
        "3",
        "6",
        "1",
        "{1, 2, 3}",
    ],
    0,
    success="Isso! O conjunto guarda só valores únicos: {1, 2, 3} → `len` é 3.",
    error="Chaves `{}` criam um conjunto, que descarta repetições: sobram 1, 2 e 3 → `len` 3.",
)

rodape_fases(__file__)
