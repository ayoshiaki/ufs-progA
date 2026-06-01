import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''class ContaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

c = ContaBancaria(100)
c.depositar(50)
print(c.saldo)''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `150`.",
    True,
    success="Isso! A conta nasce com 100; `depositar(50)` soma 50 ao `self.saldo`, virando 150.",
    error="A conta começa com 100 e `depositar(50)` soma 50 → `self.saldo` vira 150.",
)

st.divider()

st.code(
    '''c1 = ContaBancaria(100)
c2 = ContaBancaria(0)
c1.depositar(30)
print(c2.saldo)''',
    language="python",
)

stb.single_choice(
    "O que `print(c2.saldo)` mostra?",
    [
        "0",
        "30",
        "100",
        "130",
    ],
    0,
    success="Exato! `c1` e `c2` são objetos independentes — cada um tem o seu `saldo`. Depositar em `c1` não toca em `c2`.",
    error="`c1` e `c2` são contas separadas. Mexer em `c1` não muda `c2`, que continua com 0.",
)

rodape_fases(__file__)
