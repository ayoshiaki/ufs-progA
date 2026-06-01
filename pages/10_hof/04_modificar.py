import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
A função `aplicar_a_todos(funcao, lista)` deveria aplicar a **função recebida**
a cada item. Mas o modelo ignora `funcao` e soma `1` fixo. **Troque** a operação
fixa por uma chamada à `funcao`.

Para `funcao = lambda x: x * 10` e `lista = [1, 2, 3]`, o programa deve imprimir:

```
[10, 20, 30]
```
"""
)

exercicio_saida(
    chave="t10_modificar",
    enunciado="Use o parâmetro `funcao` em vez da operação fixa `item + 1`.",
    esperado="[10, 20, 30]",
    modelo=(
        "def aplicar_a_todos(funcao, lista):\n"
        "    resultado = []\n"
        "    for item in lista:\n"
        "        resultado.append(item + 1)   # <- fixo: ignora 'funcao'\n"
        "    return resultado\n"
        "\n"
        "print(aplicar_a_todos(lambda x: x * 10, [1, 2, 3]))"
    ),
    dica="Troque `item + 1` por `funcao(item)`. Assim a ação passada é que decide o resultado.",
)

rodape_fases(__file__)
