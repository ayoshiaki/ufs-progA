import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)

st.code(
    '''soma = 0
for n in [10, 20, 30]:
    soma = soma + n
print(soma)''',
    language="python",
)

stb.single_choice(
    "O que esse programa imprime?",
    ["10", "30", "60", "[10, 20, 30]"],
    2,
    success="Isso! A cada volta `soma` acumula: 0→10→30→60.",
    error="Acompanhe `soma` em cada volta do laço, começando do 0.",
)

st.divider()

st.code(
    '''for i in range(3):
    print(i)''',
    language="python",
)

stb.single_choice(
    "E aqui, o que aparece (uma por linha)?",
    ["1 2 3", "0 1 2", "0 1 2 3", "3"],
    1,
    success="Exato! `range(3)` gera 0, 1, 2 — começa no 0 e NÃO inclui o 3.",
    error="`range(n)` vai de 0 até n-1. Quantos números são, e quais?",
)

st.divider()
st.markdown("Agora um laço **`while`** — ele repete enquanto a condição for verdadeira:")

st.code(
    '''n = 5
while n > 0:
    print(n)
    n = n - 2''',
    language="python",
)

stb.single_choice(
    "O que aparece (uma por linha)?",
    [
        "5 3 1",
        "5 4 3 2 1",
        "5 3 1 -1",
        "laço infinito",
    ],
    0,
    success="Isso! `n` vale 5, 3, 1; depois vira -1, e `-1 > 0` é falso — o laço para.",
    error="Acompanhe `n`: 5 (imprime), 3 (imprime), 1 (imprime), depois -1 → `-1 > 0` é falso, para.",
)

rodape_fases(__file__)
