import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** ler as **notas** de uma turma que vieram de um arquivo e
calcular a média — mas o mundo real é bagunçado: pode haver uma linha em branco,
um `"falta"` no lugar de um número, ou o arquivo pode nem existir.

Para lidar com isso, duas ideias:

- **Arquivos** — abrir e ler com `with open("notas.txt") as f:`
- **Tratamento de erros** — `try/except` para não deixar o programa quebrar
  quando aparece um dado inválido

```python
try:
    nota = float(linha)
except ValueError:
    pass   # ignora linhas que não são número
```

> 💭 **Pense antes de avançar:** se uma única linha do arquivo tiver `"abc"`,
> faz sentido o programa inteiro parar com erro? Ou é melhor *pular* essa linha
> e seguir somando as válidas?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
