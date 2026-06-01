import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Pequena mudança, grande aprendizado. Parta do conversor e troque a temperatura
para **100 °C** (a água fervendo).

O programa deve imprimir:

```
212.0
```
"""
)

exercicio_saida_sandbox(
    chave="t2_modificar",
    enunciado="Modifique o valor de `c` para converter 100 °C.",
    esperado="212.0",
    modelo=(
        "c = 20\n"
        "f = c * 9 / 5 + 32\n"
        "print(f)"
    ),
    dica="Troque `c = 20` por `c = 100`. A fórmula continua a mesma.",
)

rodape_fases(__file__)
