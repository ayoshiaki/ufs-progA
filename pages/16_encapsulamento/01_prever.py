import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia cada trecho **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

c = ContaBancaria(100)
c.depositar(50)
print(c.saldo)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "150",
        "100",
        "50",
        "Erro: saldo é só leitura",
    ],
    0,
    success="Isso! `depositar(50)` soma ao `_saldo` (50 é positivo); `c.saldo` lê o valor: 150.",
    error="`depositar(50)` aceita (50 > 0) e soma; `c.saldo` lê o `_saldo`, que virou 150.",
)

st.divider()
st.markdown("Mesma classe. E agora?")

st.code(
    '''c = ContaBancaria(100)
c.depositar(-30)     # valor negativo
print(c.saldo)''',
    language="python",
)

stb.single_choice(
    "O que aparece?",
    [
        "100",
        "70",
        "-30",
        "130",
    ],
    0,
    success="Exato! `-30` não é positivo, então o `if valor > 0` barra a operação — o saldo continua 100.",
    error="O `depositar` só soma se `valor > 0`. Como -30 não passa, o saldo não muda: 100.",
)

st.divider()
st.markdown("E se alguém tentar mexer no saldo **direto**?")

st.code(
    '''c = ContaBancaria(100)
c.saldo = 9999
print(c.saldo)''',
    language="python",
)

stb.single_choice(
    "O que acontece?",
    [
        "Dá erro: `saldo` é uma property só de leitura (não dá para atribuir).",
        "Imprime `9999` — a atribuição funciona normalmente.",
        "Imprime `100` e ignora silenciosamente.",
        "Soma: imprime `10099`.",
    ],
    0,
    success="Isso! Como `saldo` é uma `@property` sem setter, `c.saldo = 9999` levanta `AttributeError`. É o encapsulamento protegendo o dado.",
    error="`saldo` é uma property de leitura; atribuir (`c.saldo = ...`) dá `AttributeError`. O saldo só muda pelos métodos.",
)

rodape_fases(__file__)
