import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme rodando. A compreensão abaixo lê cada número de `numeros` e
multiplica por 10, construindo uma lista nova.
"""
)

exercicio_saida(
    chave="t7_rodar",
    enunciado="Faça este programa imprimir `[10, 20, 30]`.",
    esperado="[10, 20, 30]",
    modelo=(
        "numeros = [1, 2, 3]\n"
        "dobrados = [n * 10 for n in numeros]\n"
        "print(dobrados)"
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** a compreensão `[n * 10 for n in numeros]` é exatamente
equivalente a este laço — só que numa linha:

```python
dobrados = []
for n in numeros:
    dobrados.append(n * 10)
```

Os dois constroem a **mesma** lista. A compreensão só é mais curta e direta.
"""
)

rodape_fases(__file__)
