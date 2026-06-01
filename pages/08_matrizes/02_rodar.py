import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Confirme sua previsão. Este programa percorre o tabuleiro com um **laço dentro de
laço** e conta o **total de minas**. Deve imprimir `3`.
"""
)

exercicio_saida(
    chave="t8_rodar",
    enunciado="Rode a contagem de minas.",
    esperado="3",
    modelo=(
        "tabuleiro = [\n"
        "    [0, 1, 0],\n"
        "    [0, 0, 1],\n"
        "    [1, 0, 0],\n"
        "]\n"
        "total = 0\n"
        "for linha in tabuleiro:\n"
        "    for celula in linha:\n"
        "        total = total + celula\n"
        "print(total)"
    ),
    dica="É só rodar. O laço de fora pega cada linha; o de dentro, cada célula da linha.",
)

st.info(
    "🔑 Padrão da **matriz**: um laço externo para as **linhas** e um laço interno "
    "para as **colunas** de cada linha. Quase toda operação 2D nasce desse encaixe."
)

rodape_fases(__file__)
