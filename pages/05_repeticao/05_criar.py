import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
A **lista de números** `notas` **já existe** — calcule a média e guarde em
`_res`. Se a lista estiver vazia, guarde `0`.

O código roda numa **sandbox no seu navegador** (WebAssembly). Feche todos os
testes para liberar o comprovante.
"""
)

exercicio_script_sandbox(
    chave="t5_criar",
    enunciado="Calcule a média de `notas` e guarde em `_res`:",
    casos=[
        ({"notas": [10, 20, 30]}, 20.0),
        ({"notas": [5, 5, 5, 5]}, 5.0),
        ({"notas": [7]}, 7.0),
        ({"notas": []}, 0),
    ],
    modelo="# a lista esta na variavel notas.\n# Calcule a media (ou 0 se vazia) e guarde em _res.\n_res = 0",
    dica="Some num laco (ou use sum) e divida por len. Trate a lista vazia ANTES de dividir.",
    nome_tarefa="tema5_media",
)

rodape_fases(__file__)
rodape_tema(__file__)
