import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''preco = 5
quantidade = 3
total = preco * quantidade
print("Total:", total)''',
    language="python",
)

stb.true_or_false(
    "Este programa vai imprimir exatamente: `Total: 15`",
    True,
    success="Isso! `5 * 3` dá 15, e o `print` mostra o texto seguido do número.",
    error="Releia: `total` recebe `preco * quantidade`. Quanto é 5 × 3?",
)

st.divider()

st.code(
    '''nome = "Ana"
idade = 20
print("nome")
print(idade)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "Ana\\n20",
        "nome\\n20",
        "nome\\nidade",
        "Ana\\nidade",
    ],
    1,
    success='Exato! `print("nome")` imprime o texto literal entre aspas, não o valor da variável. Já `print(idade)` imprime o valor 20.',
    error='Atenção às aspas: `"nome"` é um texto literal; `idade` (sem aspas) é a variável.',
)

rodape_fases(__file__)
