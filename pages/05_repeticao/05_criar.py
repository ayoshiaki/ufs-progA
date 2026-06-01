import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Escreva a função `media(notas)` que recebe uma **lista de números** e devolve a
média. Se a lista estiver vazia, devolva `0`.

O código roda numa **sandbox no seu navegador** (WebAssembly). Feche todos os
testes para liberar o comprovante.
"""
)

exercicio_funcao_sandbox(
    chave="t5_criar",
    enunciado="Implemente `media(notas)`:",
    func_name="media",
    cases=[(([10, 20, 30],), 20.0), (([5, 5, 5, 5],), 5.0), (([7],), 7.0), (([],), 0)],
    modelo="def media(notas):\n    # seu codigo aqui\n    return 0",
    dica="Some num laco (ou use sum) e divida por len. Trate a lista vazia ANTES de dividir.",
    nome_tarefa="tema5_media",
)

rodape_fases(__file__)
rodape_tema(__file__)
