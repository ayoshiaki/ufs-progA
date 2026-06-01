import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''def dobro(x):
    return x * 2

print(dobro(5))''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `10`.",
    True,
    success="Isso! `dobro(5)` devolve `5 * 2 = 10`, e o `print` mostra esse valor.",
    error="A função `dobro` devolve `x * 2`. Com `x = 5`, isso é 10.",
)

st.divider()

st.code(
    '''def saudacao(nome):
    print("Olá,", nome)

resultado = saudacao("Ana")
print(resultado)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "Olá, Ana\\nNone",
        "Olá, Ana\\nAna",
        "Olá, Ana",
        "None",
    ],
    0,
    success="Exato! A função usa `print` mas não tem `return`, então ela devolve `None`. Por isso `resultado` vale `None`.",
    error="A função imprime, mas NÃO tem `return` — então devolve `None`. Guardar isso em `resultado` mostra `None`.",
)

rodape_fases(__file__)
