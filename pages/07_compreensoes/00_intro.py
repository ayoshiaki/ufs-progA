import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** você tem uma lista de preços e quer construir **outra**
lista — cada preço com 10% de imposto. Você já sabe fazer isso com um laço:

```python
com_imposto = []
for p in precos:
    com_imposto.append(p * 1.1)
```

A **compreensão de lista** faz o mesmo numa linha, lendo quase como português
("para cada `p` em `precos`, calcule `p * 1.1`"):

```python
com_imposto = [p * 1.1 for p in precos]
```

Dá para **filtrar** no mesmo movimento, com um `if` no fim — só os itens que
passam no teste entram:

```python
caros = [p for p in precos if p > 100]
```

A mesma ideia vale para outras coleções:

- **Conjunto** (`set`) — uma coleção de itens **únicos** e **sem ordem**, escrita
  com chaves: `{1, 2, 3}`. É ótima para **remover duplicatas**. A *compreensão
  de conjunto* troca os colchetes por chaves:

  ```python
  tamanhos = {len(nome) for nome in nomes}   # só os tamanhos distintos
  ```

- **Dicionário** — pares `chave: valor`. A *compreensão de dicionário* usa
  chaves com os dois-pontos:

  ```python
  tamanho_de = {nome: len(nome) for nome in nomes}
  ```

> 💭 **Pense antes de avançar:** `[n * 2 for n in [1, 2, 3]]` constrói qual
> lista? E se a lista de entrada tivesse o número repetido, qual coleção
> (`[]` ou `{}`) eliminaria a repetição?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
