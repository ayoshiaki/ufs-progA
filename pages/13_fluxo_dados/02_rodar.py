import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme rodando um **pipeline** completo: a partir de `numeros`, manter os
pares (`filter`), dobrá-los (`map`) e somar tudo (`reduce`).
"""
)

exercicio_saida_sandbox(
    chave="t13_rodar",
    enunciado="Faça este programa imprimir `12`.",
    esperado="12",
    modelo=(
        "from functools import reduce\n"
        "\n"
        "numeros = [1, 2, 3, 4, 5]\n"
        "pares = filter(lambda n: n % 2 == 0, numeros)\n"
        "dobrados = map(lambda n: n * 2, pares)\n"
        "total = reduce(lambda a, b: a + b, dobrados)\n"
        "print(total)"
    ),
    dica="Já está pronto no modelo — é só rodar. Os pares 2 e 4 viram 4 e 8; somados dão 12.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** os dados passam por uma esteira de três etapas — primeiro
`filter` (peneira), depois `map` (transforma), por fim `reduce` (agrega num só).
Repare que `reduce` precisa do `from functools import reduce` lá no topo.
"""
)

rodape_fases(__file__)
