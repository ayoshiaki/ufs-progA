import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** você escreve quase o mesmo laço várias vezes — percorrer
uma lista e fazer *algo* com cada item. Só muda **o que** se faz: dobrar, elevar
ao quadrado, deixar maiúsculo... O laço é igual; a *ação* é diferente.

E se a **ação** fosse mais um argumento? Em Python, **funções são valores**:
podem ser guardadas em variáveis e **passadas como argumento** para outra função.
Uma função que recebe (ou devolve) outra função é uma **função de ordem
superior** (HOF).

```python
def aplicar(f, x):
    return f(x)        # 'f' é uma função que chegou como argumento
```

Para ações curtas existe a `lambda`: uma função **sem nome**, escrita numa linha.
`lambda x: x * 2` é o mesmo que uma função que recebe `x` e devolve `x * 2`.

> 💭 **Pense antes de avançar:** se `aplicar(f, x)` faz `return f(x)`, o que
> imprime `aplicar(lambda n: n + 1, 9)`? A função recebida soma 1 ao que receber.
"""
)

st.markdown(
    """
**E o outro lado:** uma função também pode **devolver** outra função — ela
*fabrica* uma função sob medida e a entrega pronta.

```python
def multiplicador(n):
    def multiplica(x):
        return x * n      # 'multiplica' lembra o 'n' que chegou
    return multiplica

dobro = multiplicador(2)   # fabrica uma função que multiplica por 2
print(dobro(5))            # 10
```

Repare: `multiplicador(2)` **não multiplica nada ainda** — ele monta uma função
nova (que multiplica por `2`) e a devolve. Guardamos essa função em `dobro` e só
então a chamamos. A função interna *lembra* o `n` que recebeu — isso se chama
**fechamento** (*closure*).

> 💭 **Pense antes de avançar:** se `triplo = multiplicador(3)`, quanto imprime
> `triplo(10)`? E `multiplicador(3)` sozinho — é um número ou uma função?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
