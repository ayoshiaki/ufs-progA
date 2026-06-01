import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** validar e formatar textos — por exemplo, descobrir se
uma palavra é um **palíndromo** (lê-se igual de trás para frente, como *arara*).

Texto, em programação, é uma **string** (`str`). E strings têm superpoderes:

- **indexação e fatiamento** — `texto[0]`, `texto[::-1]` (inverte!)
- **métodos** — `.lower()`, `.upper()`, `.strip()`, `.replace()`, `.split()`
- **tamanho** — `len(texto)`
- **f-strings** — montar texto com valores embutidos: `f"Olá, {nome}!"`

**Montando textos com f-strings.** Para juntar texto com valores, em vez de
`print("Oi,", nome)` (com vírgulas) use uma **f-string**: ponha um `f` antes das
aspas e escreva o que quiser mostrar entre chaves `{ }`.

```python
nome = "Ana"
idade = 20
print(f"{nome} tem {idade} anos")   # Ana tem 20 anos
```

Dentro das chaves cabe qualquer **expressão**, não só um nome de variável:

```python
print(f"O dobro de {idade} é {idade * 2}")   # O dobro de 20 é 40
```

**Formatando o valor.** Depois da expressão, um `:` abre um *molde* que ajusta
como o valor aparece — ótimo para dinheiro, médias e porcentagens:

```python
preco = 7.5
print(f"R$ {preco:.2f}")     # R$ 7.50      -> sempre 2 casas decimais
print(f"{1000000:,}")        # 1,000,000    -> separador de milhar
print(f"{0.25:.0%}")         # 25%          -> vira porcentagem
```

Dá ainda para reservar uma **largura** e **alinhar** — útil para montar colunas:

```python
print(f"{'Ana':<8}|")        # 'Ana     |'  -> à esquerda, largura 8
print(f"{42:>5}")            # '   42'       -> à direita, largura 5
print(f"{7:03d}")            # '007'         -> preenche com zeros
```

> 💭 **Pense antes de avançar:** "Arara" começa com A maiúsculo e "arara"
> com minúsculo. Para o computador, esses dois textos são *iguais*? Se não,
> como fazer a comparação ignorar maiúsculas/minúsculas?
"""
)

st.caption(
    "📖 **Documentação oficial do Python:** [Métodos de texto (`str`)](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
