import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Esta compreensão deveria manter **só os números pares**, mas está **sem o
filtro** — por isso devolve todos. **Acrescente** o `if` que mantém apenas os
pares.

O programa deve imprimir:

```
[2, 4, 6, 8, 10]
```
"""
)

exercicio_saida_sandbox(
    chave="t7_modificar",
    enunciado="Adicione o filtro `if n % 2 == 0` à compreensão.",
    esperado="[2, 4, 6, 8, 10]",
    modelo=(
        "pares = [n for n in range(1, 11)]   # <- falta o filtro\n"
        "print(pares)"
    ),
    dica="Acrescente a condição no fim: `[n for n in range(1, 11) if n % 2 == 0]`.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** sem o `if`, a compreensão copia todos os itens. O filtro
no fim é o que decide **quais** entram — aqui, só os pares.
"""
)

rodape_fases(__file__)
