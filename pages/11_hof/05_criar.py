import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho — agora **fabricando** uma função. Escreva uma **função
de ordem superior** `criar_multiplicador(n)` que **devolve** uma nova função:
essa função recebe um `x` e devolve `x * n`.

Exemplo: `criar_multiplicador(2)` devolve uma função que dobra — aplicada a `5`,
dá `10`. Já `criar_multiplicador(10)` aplicada a `5` dá `50`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_expressoes_sandbox(
    chave="t11_criar",
    enunciado="Implemente a função `criar_multiplicador`:",
    cases=[
        ("_res = criar_multiplicador(2)(5)", 10),
        ("_res = criar_multiplicador(10)(5)", 50),
        ("_res = criar_multiplicador(3)(3)", 9),
        ("_res = criar_multiplicador(0)(99)", 0),
    ],
    modelo=(
        "def criar_multiplicador(n):\n"
        "    # defina aqui dentro uma função que recebe x e devolve x * n,\n"
        "    # e DEVOLVA essa função (sem chamá-la)\n"
        "    return None"
    ),
    dica="Dentro de `criar_multiplicador`, escreva `def multiplica(x): return x * n` e depois `return multiplica`. Não chame a função — devolva-a.",
    nome_tarefa="tema11_criar_multiplicador",
)

rodape_fases(__file__)
rodape_tema(__file__)
