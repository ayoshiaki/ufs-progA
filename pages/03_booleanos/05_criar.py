import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `pode_entrar(idade, tem_ingresso)`
que **devolva** (com `return`) o booleano da regra da portaria: pode entrar quem
tem **18 anos ou mais** **e** está **com ingresso**.

Repare que você não precisa de `if` aqui — basta **devolver a expressão**
booleana, que já vale `True` ou `False`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t3_criar",
    enunciado="Implemente a função `pode_entrar`:",
    func_name="pode_entrar",
    cases=[
        ((18, True), True),
        ((17, True), False),
        ((20, False), False),
        ((30, True), True),
        ((18, False), False),
    ],
    modelo=(
        "def pode_entrar(idade, tem_ingresso):\n"
        "    # devolva a expressao: idade >= 18 E tem_ingresso\n"
        "    return False"
    ),
    dica="Devolva diretamente a expressao `idade >= 18 and tem_ingresso`.",
    nome_tarefa="tema3_pode_entrar",
)

rodape_fases(__file__)
rodape_tema(__file__)
