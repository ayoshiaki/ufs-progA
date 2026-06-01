import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. O `tabuleiro` (lista de listas de `0`/`1`) **já
existe** — monte em `_res` uma **lista com o número de minas de cada linha**.

Por exemplo, para `[[0, 1, 0], [1, 1, 0]]` o resultado é `[1, 2]` (a 1ª linha tem
1 mina; a 2ª tem 2).

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t8_criar",
    enunciado="Monte em `_res` a lista de minas por linha:",
    casos=[
        ({"tabuleiro": [[0, 1, 0], [1, 1, 0]]}, [1, 2]),
        ({"tabuleiro": [[0, 0], [0, 0]]}, [0, 0]),
        ({"tabuleiro": [[1, 1, 1]]}, [3]),
        ({"tabuleiro": [[1], [0], [1]]}, [1, 0, 1]),
    ],
    modelo=(
        "# tabuleiro e uma lista de listas de 0/1.\n"
        "# Monte em _res a lista com a quantidade de minas (1s) de cada linha.\n"
        "_res = []"
    ),
    dica="Cada linha é uma lista, e `sum(linha)` conta os 1s dela. "
         "Uma compreensão resolve: `_res = [sum(linha) for linha in tabuleiro]`.",
    nome_tarefa="tema8_minas_por_linha",
)

rodape_fases(__file__)
rodape_tema(__file__)
