import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** a portaria de um show precisa decidir, para cada pessoa,
se ela **pode entrar**. A regra: ter **18 anos ou mais** **e** estar **com
ingresso**.

Essa decisão é um valor **booleano** (`bool`): ou `True` (pode) ou `False` (não
pode). Antes de aprender a *agir* sobre a decisão — no **Tema 4 (Condicionais)**
e no `while` do **Tema 5 (Repetição)** — vamos dominar a **expressão** que produz
esse `True`/`False`.

Duas ferramentas montam essas expressões:

- **Comparações** — `==` (igual), `!=` (diferente), `<`, `>`, `<=`, `>=`. Cada
  comparação devolve `True` ou `False`: `idade >= 18`.
- **Operadores lógicos** — combinam condições:
  - `and` — `True` só se **as duas** forem verdadeiras
  - `or` — `True` se **pelo menos uma** for verdadeira
  - `not` — **inverte** (`not True` é `False`)

A regra da portaria vira uma linha: `idade >= 18 and tem_ingresso`.

**Cuidado: `=` não é `==`.** Um `=` **atribui** (`idade = 18`); dois `==`
**comparam** (`idade == 18` pergunta "são iguais?").

**Precedência lógica:** `not` age antes de `and`, que age antes de `or`. Na
dúvida, use parênteses: `(a and b) or c`.

> 💭 **Pense antes de avançar:** se alguém tem 17 anos mas está com ingresso,
> `idade >= 18 and tem_ingresso` é `True` ou `False`? Por quê?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
