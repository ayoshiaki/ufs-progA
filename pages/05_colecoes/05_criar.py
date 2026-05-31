import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `buscar_telefone(agenda, nome)`
que **devolva** (com `return`):

- o telefone, se o `nome` estiver na `agenda`;
- o texto `"não encontrado"`, se não estiver.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t5_criar",
    enunciado="Implemente a função `buscar_telefone`:",
    func_name="buscar_telefone",
    cases=[
        (({"Ana": "99991111", "Bia": "98882222"}, "Ana"), "99991111"),
        (({"Ana": "99991111", "Bia": "98882222"}, "Bia"), "98882222"),
        (({"Ana": "99991111", "Bia": "98882222"}, "Carlos"), "não encontrado"),
    ],
    modelo=(
        "def buscar_telefone(agenda, nome):\n"
        "    # dica: o metodo .get pode ajudar\n"
        '    return "não encontrado"'
    ),
    dica='Uma forma direta: `return agenda.get(nome, "não encontrado")`.',
    nome_tarefa="tema5_buscar_telefone",
)

rodape_tema(__file__)
