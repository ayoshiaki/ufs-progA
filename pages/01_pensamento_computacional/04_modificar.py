import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida

st.subheader("Fase 4 — 🔧 Modificar")
st.markdown(
    """
Pequena mudança, grande aprendizado. Parta do programa que você já conhece e
**adicione um desconto fixo de R$ 2** sobre o total.

O programa deve imprimir, para `preco = 5` e `quantidade = 3`:

```
Total com desconto: 13
```
"""
)

exercicio_saida(
    chave="t1_modificar",
    enunciado="Modifique o código para aplicar o desconto e ajustar a mensagem.",
    esperado="Total com desconto: 13",
    modelo=(
        "preco = 5\n"
        "quantidade = 3\n"
        "total = preco * quantidade\n"
        "# adicione aqui o desconto de 2\n"
        'print("Total:", total)'
    ),
    dica="Crie `total = total - 2` (ou `total -= 2`) antes do print, e troque o texto da mensagem.",
)
