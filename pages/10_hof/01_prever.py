import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''def aplicar(f, x):
    return f(x)

def quadrado(n):
    return n * n

print(aplicar(quadrado, 4))''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `16`.",
    True,
    success="Isso! `aplicar(quadrado, 4)` chama `quadrado(4)`, que devolve `16`.",
    error="`aplicar(f, x)` devolve `f(x)`. Aqui `f` é `quadrado`, então é `quadrado(4) = 16`.",
)

st.divider()

st.code(
    '''dobro = lambda n: n * 2
print(dobro(5))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "10",
        "lambda n: n * 2",
        "5",
        "Erro: lambda não pode ser guardada numa variável",
    ],
    0,
    success="Exato! `lambda n: n * 2` é uma função; guardada em `dobro`, `dobro(5)` devolve `10`.",
    error="A `lambda` é uma função comum, só que sem nome. `dobro` virou essa função, então `dobro(5) = 10`.",
)

rodape_fases(__file__)
