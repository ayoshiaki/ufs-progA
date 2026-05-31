import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida

st.subheader("Fase 4 — 🔧 Modificar")
st.markdown(
    """
Vamos deixar a comparação robusta. Parta do código abaixo e faça ele **ignorar
maiúsculas/minúsculas** antes de comparar, para que `"Arara"` seja reconhecida
como palíndromo.

O programa deve imprimir:

```
True
```
"""
)

exercicio_saida(
    chave="t6_modificar",
    enunciado="Use `.lower()` para que `Arara` seja reconhecida como palíndromo.",
    esperado="True",
    modelo=(
        'palavra = "Arara"\n'
        "# deixe a palavra minuscula antes de comparar\n"
        "print(palavra == palavra[::-1])"
    ),
    dica="Crie `palavra = palavra.lower()` logo após a primeira linha.",
)
