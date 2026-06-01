import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode a classe `ContaBancaria`, crie uma conta com 100 e deposite
50. A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t14_rodar",
    enunciado="Faça este programa imprimir `150`.",
    esperado="150",
    modelo=(
        "class ContaBancaria:\n"
        "    def __init__(self, saldo):\n"
        "        self.saldo = saldo\n"
        "\n"
        "    def depositar(self, valor):\n"
        "        self.saldo = self.saldo + valor\n"
        "\n"
        "c = ContaBancaria(100)\n"
        "c.depositar(50)\n"
        "print(c.saldo)"
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** `c.depositar(50)` não passa nada para o `self` — o Python
faz isso por você. `self` *é* o objeto `c`. Por isso `self.saldo` lá dentro é o
mesmo `c.saldo` aqui fora.
"""
)

rodape_fases(__file__)
