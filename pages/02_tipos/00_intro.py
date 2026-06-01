import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** um aplicativo de viagem precisa converter a temperatura
de **Celsius para Fahrenheit** para mostrar ao turista.

A fórmula é conhecida: `F = C × 9/5 + 32`. Mas para o computador acertar a
conta, três ideias entram em jogo:

- **Tipos** — `int` (inteiro), `float` (decimal), `str` (texto) e `bool`
  (`True`/`False`)
- **Operadores** — `+`, `-`, `*`, `/`, `//` (divisão inteira), `%` (resto) e
  `**` (potência)
- **Conversão** — `int("20")`, `float(3)`, `str(7)` trocam o tipo de um valor

**Os quatro tipos básicos.** Todo valor tem um tipo — você descobre qual com
`type(valor)`:

```python
type(10)      # int    -> inteiro
type(3.14)    # float  -> decimal
type("oi")    # str    -> texto
type(True)    # bool   -> verdadeiro/falso
```

`bool` (de *booleano*) só tem dois valores, `True` e `False`, e é o que nasce de
uma comparação: `10 > 3` vale `True`.

**Precedência: quem vem primeiro.** Numa expressão com vários operadores, o
Python não calcula só da esquerda para a direita — ele segue uma ordem de
prioridade (como na matemática):

1. `( )` — parênteses primeiro (servem para **forçar** a ordem)
2. `**` — potência
3. `*`, `/`, `//`, `%` — multiplicação, divisões e resto
4. `+`, `-` — soma e subtração

Por isso `2 + 3 * 4` é `14` (faz `3 * 4` antes), e não `20`. Quando quiser mudar
a ordem, use parênteses: `(2 + 3) * 4` é `20`. É isso que faz a fórmula
`c * 9 / 5 + 32` calcular `c * 9 / 5` antes do `+ 32`.

> 💭 **Pense antes de avançar:** quanto é `9/5` em Python? E `9//5`? Um desses
> resultados tem casas decimais e o outro não — essa diferença é o coração
> deste tema.
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
