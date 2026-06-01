import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** guardar o tabuleiro de um **campo minado** — uma grade
com **linhas** e **colunas**, onde cada célula tem `1` (mina) ou `0` (vazio).

Uma lista comum é uma fila de valores; um tabuleiro é uma **tabela**. A ideia é
usar uma **lista de listas**: cada **linha** é uma lista, e o tabuleiro é a lista
das linhas.

```python
tabuleiro = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
]
```

- **Acessar uma célula** usa **dois índices**: `tabuleiro[linha][coluna]`.
  `tabuleiro[1][2]` é a linha `1`, coluna `2` → `1` (tem mina). **O primeiro
  índice é a linha; o segundo, a coluna.**
- **Dimensões:** `len(tabuleiro)` é o número de **linhas**; `len(tabuleiro[0])`,
  o número de **colunas**.
- **Percorrer tudo** pede um **laço dentro de laço** (aninhado):

  ```python
  for linha in tabuleiro:        # cada linha é uma lista
      for celula in linha:       # cada célula é um valor
          print(celula)
  ```

- **Construir** um tabuleiro vazio com **compreensão** (Tema 7): `[[0] * 3 for _
  in range(3)]` cria 3 linhas de 3 zeros. *(Cuidado: `[[0] * 3] * 3` parece igual,
  mas as três linhas viram a MESMA lista — mexer numa mexe em todas.)*

> 💭 **Pense antes de avançar:** no tabuleiro acima, qual é o valor de
> `tabuleiro[2][0]`? E quantas linhas e colunas ele tem?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
