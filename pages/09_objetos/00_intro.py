import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** modelar uma **conta bancária** que guarda um saldo e
permite **depositar** e **sacar**. Em vez de espalhar variáveis soltas
(`saldo_da_ana`, `saldo_do_caio`...), juntamos *dados* e *ações* num mesmo lugar:
um **objeto**.

Para isso usamos uma **classe** — a "planta" do objeto:

- **atributos** — os dados que o objeto guarda (`self.saldo`)
- **métodos** — as ações que o objeto sabe fazer (`depositar`, `sacar`)
- **`__init__`** — o "construtor", que prepara o objeto quando ele nasce
- **`self`** — o próprio objeto, por dentro dos métodos

```python
class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo
```

> 💭 **Pense antes de avançar:** duas contas diferentes (`c1` e `c2`) têm cada
> uma o seu próprio `saldo`. O que no código garante que mexer em `c1` não
> altera `c2`?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
