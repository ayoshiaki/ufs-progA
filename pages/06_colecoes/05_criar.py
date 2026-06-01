import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. O dicionário `agenda` e o `nome` procurado **já
existem** — guarde em `_res`:

- o telefone, se o `nome` estiver na `agenda`;
- o texto `"não encontrado"`, se não estiver.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t6_criar",
    enunciado="Busque `nome` na `agenda` e guarde o resultado em `_res`:",
    casos=[
        ({"agenda": {"Ana": "99991111", "Bia": "98882222"}, "nome": "Ana"}, "99991111"),
        ({"agenda": {"Ana": "99991111", "Bia": "98882222"}, "nome": "Bia"}, "98882222"),
        ({"agenda": {"Ana": "99991111", "Bia": "98882222"}, "nome": "Carlos"}, "não encontrado"),
    ],
    modelo=(
        "# agenda (dicionario) e nome ja existem.\n"
        "# Guarde em _res o telefone, ou \"nao encontrado\".\n"
        '_res = "não encontrado"'
    ),
    dica='Uma forma direta: `_res = agenda.get(nome, "não encontrado")`.',
    nome_tarefa="tema6_buscar_telefone",
)

rodape_fases(__file__)
rodape_tema(__file__)
