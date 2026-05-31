import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida

st.subheader("Fase 4 — 🔧 Modificar")
st.markdown(
    """
Falta uma forma. **Crie a classe** `Circulo`, que também herda de `Forma`, com
um raio e o seu próprio `area()` (use `3.14159` para π).

Para um círculo de raio 2, o programa deve imprimir (área ≈ 12.57):

```
12.57
```
"""
)

exercicio_saida(
    chave="t10_modificar",
    enunciado="Crie a classe `Circulo(Forma)` com seu próprio `area()`.",
    esperado="12.57",
    modelo=(
        "class Forma:\n"
        "    def area(self):\n"
        "        return 0\n"
        "\n"
        "# crie aqui a classe Circulo(Forma) com __init__(self, raio) e area(self)\n"
        "\n"
        "c = Circulo(2)\n"
        "print(round(c.area(), 2))"
    ),
    dica="`class Circulo(Forma):` com `__init__(self, raio): self.raio = raio` e `area(self): return 3.14159 * self.raio * self.raio`.",
)
