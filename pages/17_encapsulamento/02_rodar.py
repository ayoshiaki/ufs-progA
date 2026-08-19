import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Confirme sua previsão. Esta conta está **encapsulada**: o saldo é interno
(`_saldo`), só de leitura por fora (`@property`), e muda apenas pelos métodos —
que protegem as regras. O programa tenta um saque grande demais e um depósito
negativo (ambos barrados) e deve imprimir `120`.
"""
)

exercicio_saida_sandbox(
    chave="t16_rodar",
    enunciado="Rode a conta encapsulada.",
    esperado="120",
    modelo=(
        "class ContaBancaria:\n"
        "    def __init__(self, saldo):\n"
        "        self._saldo = saldo\n"
        "\n"
        "    @property\n"
        "    def saldo(self):\n"
        "        return self._saldo\n"
        "\n"
        "    def depositar(self, valor):\n"
        "        if valor > 0:\n"
        "            self._saldo += valor\n"
        "\n"
        "    def sacar(self, valor):\n"
        "        if 0 < valor <= self._saldo:\n"
        "            self._saldo -= valor\n"
        "\n"
        "c = ContaBancaria(100)\n"
        "c.sacar(999)        # saldo insuficiente: barrado\n"
        "c.depositar(-50)    # negativo: barrado\n"
        "c.depositar(20)     # ok\n"
        "print(c.saldo)"
    ),
    dica="Já está pronto — é só rodar. Só o `depositar(20)` passa nas regras; o resto é barrado.",
)

st.info(
    "🔑 Padrão do **encapsulamento**: o dado fica **interno** (`_saldo`) e as "
    "**regras moram nos métodos**. Quem usa a classe não precisa (nem consegue) "
    "mexer no saldo direto — só pedir `depositar`/`sacar`."
)

rodape_fases(__file__)
