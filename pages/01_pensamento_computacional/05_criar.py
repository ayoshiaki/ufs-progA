import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `valor_total(preco, quantidade)`
que devolva (com `return`) o total a pagar.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t1_criar",
    enunciado="Implemente a função `valor_total`:",
    func_name="valor_total",
    cases=[((5, 3), 15), ((10, 0), 0), ((2, 4), 8), ((100, 1), 100)],
    modelo="def valor_total(preco, quantidade):\n    # seu codigo aqui\n    return 0",
    dica="O total e `preco * quantidade`. Use `return` (nao `print`).",
    nome_tarefa="tema1_valor_total",
)

rodape_fases(__file__)
rodape_tema(__file__)
