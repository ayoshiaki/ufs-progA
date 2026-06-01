import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho, montando o **pipeline** inteiro. Escreva a função
`soma_quadrados_pares(numeros)` que devolva a **soma dos quadrados dos números
pares** usando `filter`, `map` e `reduce`.

Exemplo: para `[1, 2, 3, 4]`, os pares são 2 e 4; seus quadrados, 4 e 16; a soma
é `20`.

⚠️ Atenção à lista sem pares (resultado `0`): dê um **valor inicial** ao
`reduce` para ele não quebrar com a coleção vazia.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t12_criar",
    enunciado="Implemente `soma_quadrados_pares` com filter + map + reduce:",
    func_name="soma_quadrados_pares",
    cases=[
        (([1, 2, 3, 4],), 20),
        (([2, 4],), 20),
        (([1, 3, 5],), 0),
        (([6],), 36),
        (([],), 0),
    ],
    modelo=(
        "from functools import reduce\n"
        "\n"
        "def soma_quadrados_pares(numeros):\n"
        "    # 1) filter: so os pares  2) map: ao quadrado  3) reduce: soma (inicial 0)\n"
        "    return 0"
    ),
    dica="pares = filter(lambda n: n % 2 == 0, numeros); quad = map(lambda n: n * n, pares); "
         "return reduce(lambda a, b: a + b, quad, 0). O 0 final faz a lista vazia dar 0.",
    nome_tarefa="tema12_soma_quadrados_pares",
)

rodape_fases(__file__)
rodape_tema(__file__)
