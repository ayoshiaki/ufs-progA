import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Parta do acumulador de soma e transforme-o num programa que **conta quantos
números são pares** na lista `[4, 7, 10, 3, 6]`.

Saída esperada:

```
Pares: 3
```
"""
)

exercicio_saida(
    chave="t5_modificar",
    enunciado="Modifique o laço para contar os pares.",
    esperado="Pares: 3",
    modelo=(
        "numeros = [4, 7, 10, 3, 6]\n"
        "contador = 0\n"
        "for n in numeros:\n"
        "    # se n for par, some 1 ao contador\n"
        "    pass\n"
        'print("Pares:", contador)'
    ),
    dica="Um número é par quando `n % 2 == 0`. Use um `if` dentro do laço para incrementar `contador`.",
)

rodape_fases(__file__)
