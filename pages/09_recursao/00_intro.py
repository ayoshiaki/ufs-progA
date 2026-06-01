import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** calcular o **fatorial** de um número. O fatorial de `5`
(escrito `5!`) é `5 × 4 × 3 × 2 × 1 = 120`.

Repare que esse problema se define **em termos de si mesmo**: `5!` é `5` vezes
`4!`; e `4!` é `4` vezes `3!`; e assim por diante. Quando um problema contém uma
versão menor dele mesmo, uma função pode **chamar a si mesma** para resolvê-lo —
isso é **recursão**.

Toda função recursiva precisa de duas partes:

- **Caso base** — a versão mais simples, que tem resposta direta e **para** a
  recursão. Para o fatorial: `0! = 1`.
- **Caso recursivo** — resolve o problema usando uma versão **menor** dele
  mesmo. Para o fatorial: `n! = n × (n - 1)!`.

```python
def fatorial(n):
    if n == 0:          # caso base
        return 1
    return n * fatorial(n - 1)   # caso recursivo
```

⚠️ **Sem caso base, a recursão nunca para** — a função fica chamando a si mesma
até o Python desistir com um erro (`RecursionError`). O caso base é o freio.

> 💭 **Pense antes de avançar:** já dava para fazer o fatorial com um laço `for`
> (Tema 5). Por que aprender recursão? Porque alguns problemas — como percorrer
> pastas dentro de pastas — são **naturalmente** recursivos, e a solução fica
> mais clara assim.
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
