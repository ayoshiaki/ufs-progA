import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Este programa deveria imprimir a **lista** dos quadrados, mas imprime algo como
`<map object at 0x...>` — porque `map` é **preguiçoso** e ninguém pediu o
resultado. **Conserte** embrulhando o `map` em `list(...)`.

O programa deve imprimir:

```
[1, 4, 9]
```
"""
)

exercicio_saida(
    chave="t13_modificar",
    enunciado="Embrulhe o `map` em `list(...)` para materializar a lista.",
    esperado="[1, 4, 9]",
    modelo=(
        "numeros = [1, 2, 3]\n"
        "quadrados = map(lambda n: n * n, numeros)\n"
        "print(quadrados)   # <- imprime o objeto map, nao a lista\n"
    ),
    dica="Troque `print(quadrados)` por `print(list(quadrados))` — ou guarde `list(map(...))`.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** `map` e `filter` não calculam nada até alguém **consumir**
o resultado. `list(...)` força a esteira a rodar e entrega a lista pronta.
"""
)

rodape_fases(__file__)
