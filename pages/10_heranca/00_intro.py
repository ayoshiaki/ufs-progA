import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** um editor de desenho precisa calcular a **área** de
várias formas — círculos, retângulos... — sem encher o código de `if` para cada
tipo. A orientação a objetos resolve isso com **herança** e **polimorfismo**.

- **herança** — uma classe (`Circulo`) *herda* de outra (`Forma`) e aproveita
  o que ela já tem: `class Circulo(Forma):`
- **sobrescrita** — a filha redefine um método à sua maneira (cada forma calcula
  `area()` do seu jeito)
- **polimorfismo** — você chama `forma.area()` sem saber se é círculo ou
  retângulo; cada objeto responde do jeito certo

```python
class Forma:
    def area(self):
        return 0

class Retangulo(Forma):
    def area(self):
        return self.base * self.altura
```

> 💭 **Pense antes de avançar:** se você tem uma lista misturada de círculos e
> retângulos e chama `.area()` em cada um, por que não precisa de um `if` para
> saber qual fórmula usar?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
