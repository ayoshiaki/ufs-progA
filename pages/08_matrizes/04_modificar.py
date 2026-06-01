import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Queremos saber se há uma mina na **linha 1, coluna 2**. Mas o programa está com
os índices **trocados** (`[coluna][linha]`) — e isso pega a célula errada (ou
nem existe). **Conserte** para a ordem certa `[linha][coluna]`.

Para o tabuleiro abaixo, a linha 1, coluna 2 vale `1`, então deve imprimir:

```
1
```
"""
)

exercicio_saida_sandbox(
    chave="t8_modificar",
    enunciado="Troque a ordem dos índices para `[linha][coluna]`.",
    esperado="1",
    modelo=(
        "tabuleiro = [\n"
        "    [0, 1, 0],\n"
        "    [0, 0, 1],\n"
        "    [1, 0, 0],\n"
        "]\n"
        "linha = 1\n"
        "coluna = 2\n"
        "print(tabuleiro[coluna][linha])   # <- índices trocados\n"
    ),
    dica="A ordem é linha primeiro, coluna depois: `tabuleiro[linha][coluna]`.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** `tabuleiro[coluna][linha]` aqui vira `tabuleiro[2][1]`
(linha 2, coluna 1) — outra célula. Inverter os índices é um dos erros mais
comuns com matrizes.
"""
)

rodape_fases(__file__)
