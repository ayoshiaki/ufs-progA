import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. A temperatura em Celsius **já está** na variável `c` —
converta para Fahrenheit e guarde o resultado em `_res`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t2_criar",
    enunciado="Converta `c` para Fahrenheit e guarde em `_res`:",
    casos=[
        ({"c": 0}, 32.0),
        ({"c": 100}, 212.0),
        ({"c": 20}, 68.0),
        ({"c": -40}, -40.0),
        ({"c": 25}, 77.0),
    ],
    modelo="# a temperatura em Celsius esta na variavel c.\n# Converta para Fahrenheit e guarde em _res.\n_res = 0",
    dica="A formula e `c * 9 / 5 + 32`. Guarde em `_res` (nao use print).",
    nome_tarefa="tema2_celsius_fahrenheit",
)

rodape_fases(__file__)
rodape_tema(__file__)
