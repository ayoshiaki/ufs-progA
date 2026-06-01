import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia cada trecho **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''tabuleiro = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
]
print(tabuleiro[2][0])''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "1",
        "0",
        "[1, 0, 0]",
        "Erro",
    ],
    0,
    success="Isso! `tabuleiro[2]` é a linha `[1, 0, 0]`; o `[0]` pega a coluna 0 → `1`.",
    error="Primeiro o índice da linha (2 → `[1, 0, 0]`), depois o da coluna (0 → `1`).",
)

st.divider()

st.code(
    '''print(len(tabuleiro), len(tabuleiro[0]))''',
    language="python",
)

stb.single_choice(
    "E aqui (linhas e colunas)?",
    [
        "3 3",
        "9",
        "3",
        "0 0",
    ],
    0,
    success="Exato! `len(tabuleiro)` = 3 linhas; `len(tabuleiro[0])` = 3 colunas.",
    error="`len(tabuleiro)` conta as linhas; `len(tabuleiro[0])` conta as colunas da primeira linha.",
)

st.divider()

st.code(
    '''total = 0
for linha in tabuleiro:
    for celula in linha:
        total = total + celula
print(total)''',
    language="python",
)

stb.single_choice(
    "Quantas minas o laço aninhado conta?",
    [
        "3",
        "9",
        "0",
        "6",
    ],
    0,
    success="Isso! Somando todas as células (cada mina vale 1), há 3 minas no tabuleiro.",
    error="O laço soma todas as células. Conte quantos `1` existem no tabuleiro: são 3.",
)

rodape_fases(__file__)
