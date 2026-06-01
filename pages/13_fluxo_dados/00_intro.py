import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** dada uma lista de preços, somar o total **só dos preços
acima de 100**, cada um já com 10% de imposto. Pense nos dados **fluindo** por
uma esteira, passando por etapas:

```
preços  →  filtrar (> 100)  →  transformar (× 1.1)  →  somar tudo  →  total
```

Python tem uma função para cada etapa — e todas recebem **outra função** como
argumento (é ordem superior em ação):

- **`filter(f, dados)`** — mantém só os itens em que `f(item)` é verdadeiro.
- **`map(f, dados)`** — aplica `f` a cada item, transformando-o.
- **`reduce(f, dados)`** — combina os itens **dois a dois** até sobrar um só
  (a soma, o máximo, o produto...). Vem do módulo `functools`:

```python
from functools import reduce

caros   = filter(lambda p: p > 100, precos)
com_imp = map(lambda p: p * 1.1, caros)
total   = reduce(lambda a, b: a + b, com_imp)
```

⚠️ `map` e `filter` são **preguiçosos**: não devolvem uma lista pronta, e sim um
objeto que entrega os itens sob demanda. Para **ver** o conteúdo, embrulhe em
`list(...)`: `list(map(...))`.

**Ponte com as compreensões (Tema 7):** `[p * 1.1 for p in precos if p > 100]`
já faz o `filter` + `map` num movimento só. A novidade aqui é o `reduce`, que
**agrega** a coleção inteira num único valor.

> 💭 **Pense antes de avançar:** `reduce(lambda a, b: a + b, [1, 2, 3, 4])`
> calcula `((1 + 2) + 3) + 4`. Quanto dá? E se a função fosse `a * b`?
"""
)

st.caption(
    "📖 **Documentação oficial do Python:** [`map` e `filter` (funções embutidas)](https://docs.python.org/pt-br/3/library/functions.html#map) e [`functools.reduce`](https://docs.python.org/pt-br/3/library/functools.html#functools.reduce)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
