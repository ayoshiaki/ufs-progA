import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** no Tema 15, a `ContaBancaria` guardava `self.saldo`
**público**. Nada impede um descuido (ou uma fraude) como:

```python
c = ContaBancaria(100)
c.saldo = -1000      # 😱 mexeu direto e furou a regra
```

A conta deveria **proteger** o próprio saldo: ele só pode mudar por `depositar`
e `sacar`, e nunca ficar inválido. Essa ideia é o **encapsulamento** — *esconder
os dados internos* e deixar que se mexa neles **apenas por métodos** que cuidam
das regras.

Em Python isso se faz por **convenção** e com **`@property`**:

```python
class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo          # _ no nome = "interno, não mexa direto"

    @property
    def saldo(self):                 # leitura controlada: c.saldo funciona...
        return self._saldo           # ...mas NÃO dá para fazer c.saldo = x

    def depositar(self, valor):
        if valor > 0:                # a regra mora aqui dentro
            self._saldo += valor
```

- **`_saldo`** — o underscore avisa "atributo interno"; quem usa a classe não
  deve tocar nele direto. *(Há também `__saldo`, com dois underscores, que o
  Python "embaralha" para dificultar ainda mais o acesso de fora.)*
- **`@property`** — transforma o método `saldo` num atributo de **leitura**:
  `c.saldo` lê o valor, mas tentar `c.saldo = 5` dá erro. O saldo só muda pelos
  métodos.

> 💭 **Pense antes de avançar:** se `saldo` é só leitura (`@property`) e
> `depositar` só aceita valores positivos, ainda dá para deixar a conta com
> saldo negativo de propósito?
"""
)

st.caption(
    "📖 **Documentação oficial do Python:** [Variáveis privadas](https://docs.python.org/pt-br/3/tutorial/classes.html#private-variables)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
