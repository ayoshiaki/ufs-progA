import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Este `fatorial` está **com o caso base errado**: devolve `0`, e por isso o
produto inteiro vira `0`. **Corrija o caso base** para que `fatorial(5)` dê o
valor certo.

O programa deve imprimir:

```
120
```
"""
)

exercicio_saida(
    chave="t11_modificar",
    enunciado="Conserte o caso base para que o fatorial fique correto.",
    esperado="120",
    modelo=(
        "def fatorial(n):\n"
        "    if n == 0:\n"
        "        return 0   # <- caso base errado\n"
        "    return n * fatorial(n - 1)\n"
        "\n"
        "print(fatorial(5))"
    ),
    dica="`0!` vale `1`, nao `0`. Troque o `return 0` do caso base por `return 1` "
         "(qualquer coisa vezes 0 da 0 — por isso tudo zerava).",
)

rodape_fases(__file__)
