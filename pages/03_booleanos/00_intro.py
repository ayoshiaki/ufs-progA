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

st.markdown(
    """
**Verdadeiro "de fato": truthy e falsy.** Em Python, *qualquer* valor pode ser
lido como verdadeiro ou falso — não só `True`/`False`. A função `bool(...)`
revela essa leitura:

- **Falsy** (lidos como falso): `0`, `0.0`, `""` (texto vazio) e `False`.
  *(Mais adiante você verá que `None` e coleções vazias — `[]`, `{}` — também são.)*
- **Truthy** (lidos como verdadeiro): **todo o resto** — `5`, `-1`, `"oi"`... e
  cuidado: `"0"` é um **texto não vazio**, então é **truthy**!

```python
print(bool(""))     # False
print(bool("oi"))   # True
print(not 0)        # True   — 'not' lê 0 como falso e inverte
```

**`and`/`or` não devolvem só `True`/`False` — devolvem um dos valores.** O `or`
entrega o **primeiro truthy** (ou o último valor, se todos forem falsy); o `and`,
o **primeiro falsy**. Daí um truque comum para **valor padrão**:

```python
nome = ""                    # o usuário não digitou nada
print(nome or "Anônimo")     # "Anônimo"  (nome é falsy → vai o 2º)
nome = "Ana"
print(nome or "Anônimo")     # "Ana"      (nome é truthy → fica ele mesmo)
```

> 💭 **Pense antes de avançar:** `bool("0")` é `True` ou `False`? E o que
> `"" or 0 or "fim"` devolve? *(No Tema 4, `if nome:` vai usar exatamente essa
> leitura truthy/falsy.)*
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
