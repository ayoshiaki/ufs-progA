import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. As variáveis `idade` e `tem_ingresso` **já existem** —
guarde em `_res` o booleano da regra da portaria: pode entrar quem tem **18 anos
ou mais** **e** está **com ingresso**.

Repare que você não precisa de `if` aqui — basta guardar a **expressão**
booleana, que já vale `True` ou `False`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t3_criar",
    enunciado="Guarde em `_res` o resultado da regra:",
    casos=[
        ({"idade": 18, "tem_ingresso": True}, True),
        ({"idade": 17, "tem_ingresso": True}, False),
        ({"idade": 20, "tem_ingresso": False}, False),
        ({"idade": 30, "tem_ingresso": True}, True),
        ({"idade": 18, "tem_ingresso": False}, False),
    ],
    modelo=(
        "# idade e tem_ingresso ja existem.\n"
        "# Guarde em _res o booleano: 18+ E com ingresso.\n"
        "_res = False"
    ),
    dica="Guarde diretamente a expressao: `_res = idade >= 18 and tem_ingresso`.",
    nome_tarefa="tema3_pode_entrar",
)

rodape_fases(__file__)
rodape_tema(__file__)
