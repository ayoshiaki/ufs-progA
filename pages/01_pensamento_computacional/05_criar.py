import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. As variáveis `preco` e `quantidade` **já existem** —
calcule o total a pagar e guarde em `_res`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t1_criar",
    enunciado="Calcule o total e guarde em `_res`:",
    casos=[
        ({"preco": 5, "quantidade": 3}, 15),
        ({"preco": 10, "quantidade": 0}, 0),
        ({"preco": 2, "quantidade": 4}, 8),
        ({"preco": 100, "quantidade": 1}, 100),
    ],
    modelo="# preco e quantidade ja existem.\n# Calcule o total a pagar e guarde em _res.\n_res = 0",
    dica="O total e `preco * quantidade`. Guarde em `_res` (nao use print).",
    nome_tarefa="tema1_valor_total",
)

rodape_fases(__file__)
rodape_tema(__file__)
