import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense na matriz como uma **tabela** de linhas e colunas.")

stb.single_choice(
    "Em `tabuleiro[i][j]`, o que são `i` e `j`?",
    [
        "`i` é a linha; `j` é a coluna.",
        "`i` é a coluna; `j` é a linha.",
        "Os dois são linhas; a coluna não tem índice.",
        "`i` é o valor da célula; `j` é a posição.",
    ],
    0,
    success="Isso! O primeiro índice escolhe a linha; o segundo, a coluna dentro dessa linha.",
    error="A ordem é `[linha][coluna]`: `tabuleiro[i]` pega a linha `i`; o `[j]` pega a coluna.",
)

st.divider()

stb.single_choice(
    "Como descobrir o número de **colunas** de uma matriz `m` (retangular)?",
    [
        "`len(m[0])` — o tamanho de uma linha.",
        "`len(m)` — o número de linhas.",
        "`len(m) * len(m[0])` — o total de células.",
        "Não dá para saber sem percorrer tudo.",
    ],
    0,
    success="Exato! `len(m)` conta as linhas; `len(m[0])` conta as colunas (o tamanho de uma linha).",
    error="`len(m)` são as linhas. As colunas são o tamanho de uma linha: `len(m[0])`.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre matrizes (lista de listas) estão corretas?",
    {
        "Uma matriz é uma lista cujos itens são, eles próprios, listas (as linhas).": True,
        "`m[1][2]` acessa a linha 1, coluna 2.": True,
        "Percorrer toda a matriz costuma exigir um laço dentro de outro.": True,
        "`len(m)` dá o número de linhas.": True,
        "`m[2][0]` e `m[0][2]` são sempre a mesma célula.": False,
    },
    success="Mandou bem! Linha primeiro, coluna depois; e percorrer tudo pede laço aninhado. Trocar a ordem dos índices muda a célula.",
    error="Revise: `[linha][coluna]` — `m[2][0]` (linha 2) é diferente de `m[0][2]` (linha 0).",
)

rodape_fases(__file__)
