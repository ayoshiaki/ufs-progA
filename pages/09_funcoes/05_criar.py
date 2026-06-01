import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** com **três parâmetros**,
`total_compra(preco, qtd, desconto)`, que **devolva** (com `return`) o valor a
pagar: o preço vezes a quantidade, **menos** o desconto.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t9_criar",
    enunciado="Implemente a função `total_compra`:",
    func_name="total_compra",
    cases=[
        ((10, 3, 5), 25), ((100, 1, 0), 100), ((20, 5, 20), 80), ((7, 0, 0), 0),
    ],
    modelo=(
        "def total_compra(preco, qtd, desconto):\n"
        "    # seu codigo aqui\n"
        "    return 0"
    ),
    dica="O total e `preco * qtd - desconto`. Use `return` (nao `print`).",
    nome_tarefa="tema9_total_compra",
)

rodape_fases(__file__)
rodape_tema(__file__)
