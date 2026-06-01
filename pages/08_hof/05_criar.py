import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função de ordem superior**
`aplicar_duas_vezes(funcao, valor)` que aplique `funcao` ao `valor` **duas
vezes** e **devolva** o resultado — ou seja, `funcao(funcao(valor))`.

Exemplo: com `lambda x: x + 1` e `valor = 10`, o resultado é `12` (soma 1, e
soma 1 de novo).

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_expressoes_sandbox(
    chave="t8_criar",
    enunciado="Implemente a função `aplicar_duas_vezes`:",
    cases=[
        ("_res = aplicar_duas_vezes(lambda x: x + 1, 10)", 12),
        ("_res = aplicar_duas_vezes(lambda x: x * 2, 3)", 12),
        ("_res = aplicar_duas_vezes(lambda x: x - 5, 100)", 90),
        ("_res = aplicar_duas_vezes(str.upper, 'oi')", "OI"),
    ],
    modelo=(
        "def aplicar_duas_vezes(funcao, valor):\n"
        "    # aplique 'funcao' ao 'valor', e depois de novo ao resultado\n"
        "    return valor"
    ),
    dica="Aplique uma vez: `funcao(valor)`. Aplique de novo no resultado: `funcao(funcao(valor))`. Use `return`.",
    nome_tarefa="tema8_aplicar_duas_vezes",
)

rodape_fases(__file__)
rodape_tema(__file__)
