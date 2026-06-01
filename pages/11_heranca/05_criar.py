import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva a hierarquia de formas:

- `Forma` — classe base com `area(self)` devolvendo `0`;
- `Retangulo(Forma)` — `__init__(self, base, altura)` e `area()` = base × altura;
- `Circulo(Forma)` — `__init__(self, raio)` e `area()` = `3.14159` × raio × raio.

Os testes calculam áreas e somam formas diferentes numa lista (polimorfismo).
O código roda numa **sandbox no seu navegador** (WebAssembly). Passe em todos
para liberar o comprovante de entrega.
"""
)

exercicio_expressoes_sandbox(
    chave="t11_criar",
    enunciado="Implemente `Forma`, `Retangulo` e `Circulo`:",
    cases=[
        ("_res = Retangulo(3, 4).area()", 12),
        ("_res = round(Circulo(1).area(), 2)", 3.14),
        ("_res = round(Circulo(2).area(), 2)", 12.57),
        ("formas = [Retangulo(2, 3), Circulo(1)]; _res = round(sum(f.area() for f in formas), 2)", 9.14),
    ],
    modelo=(
        "class Forma:\n"
        "    def area(self):\n"
        "        return 0\n"
        "\n"
        "class Retangulo(Forma):\n"
        "    def __init__(self, base, altura):\n"
        "        self.base = base\n"
        "        self.altura = altura\n"
        "    def area(self):\n"
        "        # base vezes altura\n"
        "        return 0\n"
        "\n"
        "class Circulo(Forma):\n"
        "    def __init__(self, raio):\n"
        "        self.raio = raio\n"
        "    def area(self):\n"
        "        # 3.14159 vezes raio ao quadrado\n"
        "        return 0"
    ),
    dica="Retangulo: `return self.base * self.altura`. Circulo: `return 3.14159 * self.raio * self.raio`.",
    nome_tarefa="tema11_formas",
)

rodape_fases(__file__)
rodape_tema(__file__)
