import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função recursiva** `soma_ate(n)` que
**devolva** (com `return`) a soma de todos os inteiros de `1` até `n`.

Por exemplo, `soma_ate(4)` é `1 + 2 + 3 + 4 = 10`.

Pense nas duas partes:
- **caso base:** `soma_ate(0)` é `0`;
- **caso recursivo:** `soma_ate(n)` é `n + soma_ate(n - 1)`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t10_criar",
    enunciado="Implemente a função recursiva `soma_ate`:",
    func_name="soma_ate",
    cases=[
        ((0,), 0),
        ((1,), 1),
        ((4,), 10),
        ((5,), 15),
        ((10,), 55),
    ],
    modelo=(
        "def soma_ate(n):\n"
        "    if n == 0:        # caso base\n"
        "        return 0\n"
        "    # caso recursivo: n + a soma ate (n - 1)\n"
        "    return 0"
    ),
    dica="No caso recursivo, devolva `n + soma_ate(n - 1)`. O caso base ja esta pronto.",
    nome_tarefa="tema10_soma_ate",
)

rodape_fases(__file__)
rodape_tema(__file__)
