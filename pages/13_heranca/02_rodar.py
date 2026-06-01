import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode a hierarquia `Forma`/`Retangulo` e calcule a área de um
retângulo 3×4. A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t13_rodar",
    enunciado="Faça este programa imprimir `12`.",
    esperado="12",
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
        "        return self.base * self.altura\n"
        "\n"
        "r = Retangulo(3, 4)\n"
        "print(r.area())"
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** `Retangulo` não repete o que `Forma` já tem — ele
**herda** e só redefine o `area()`. Quando um método existe nas duas, vale o da
classe filha (a mais específica).
"""
)

rodape_fases(__file__)
