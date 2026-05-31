import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida

st.subheader("Fase 4 — 🔧 Modificar")
st.markdown(
    """
A função `total` calcula `preco * qtd`. **Adicione um terceiro parâmetro**
`desconto` e subtraia-o do total.

Para `preco=10`, `qtd=3` e `desconto=5`, o programa deve imprimir:

```
25
```
"""
)

exercicio_saida(
    chave="t7_modificar",
    enunciado="Acrescente o parâmetro `desconto` e desconte-o do total.",
    esperado="25",
    modelo=(
        "def total(preco, qtd):\n"
        "    return preco * qtd\n"
        "\n"
        "print(total(10, 3))"
    ),
    dica="Mude a assinatura para `def total(preco, qtd, desconto):`, faça `return preco * qtd - desconto` e chame `total(10, 3, 5)`.",
)
