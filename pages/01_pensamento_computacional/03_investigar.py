import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em como o computador executa o programa.")

stb.single_choice(
    "Por que a linha `total = preco * quantidade` precisa vir DEPOIS das duas primeiras?",
    [
        "Porque multiplicação é mais lenta que atribuição.",
        "Porque o computador lê de cima para baixo e `preco`/`quantidade` precisam já existir.",
        "Por questão de estilo apenas; a ordem não muda nada.",
        "Porque o `print` exige isso.",
    ],
    1,
    success="Isso! A execução é sequencial: uma variável só pode ser usada depois de criada.",
    error="Pense na ordem de execução: o que precisa existir antes de multiplicar?",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre `print(\"Total:\", total)` estão corretas?",
    {
        "`\"Total:\"` é um texto literal (string).": True,
        "`total` é uma variável cujo valor será impresso.": True,
        "A vírgula faz o print juntar os dois com um espaço.": True,
        "O print só funciona com números.": False,
    },
    success="Mandou bem! O print aceita vários valores separados por vírgula e os mostra com espaço entre eles.",
    error="Revise: o que está entre aspas? O que a vírgula faz?",
)

st.divider()

stb.single_choice(
    "Decidir que a **cor** e a **marca** do produto não importam para o cálculo — "
    "usando só preço e quantidade — é um exemplo de qual pilar?",
    [
        "Decomposição",
        "Abstração",
        "Reconhecimento de padrões",
        "Algoritmo",
    ],
    1,
    success="Isso! **Abstração** é justamente ignorar os detalhes que não importam agora e focar no essencial.",
    error="É **abstração**: focar no essencial (preço e quantidade) e deixar de lado o que não afeta a conta (cor, marca).",
)

rodape_fases(__file__)
