import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva a **classe** `ContaBancaria` completa:

- `__init__(self, saldo)` — guarda o saldo inicial em `self.saldo`;
- `depositar(self, valor)` — soma `valor` ao saldo;
- `sacar(self, valor)` — desconta `valor`, **mas só se houver saldo suficiente**
  (se não houver, o saldo não muda).

Os testes criam contas e conferem o `saldo` depois das operações. O código roda
numa **sandbox no seu navegador** (WebAssembly). Passe em todos para liberar o
comprovante de entrega.
"""
)

exercicio_expressoes_sandbox(
    chave="t14_criar",
    enunciado="Implemente a classe `ContaBancaria`:",
    cases=[
        ("c = ContaBancaria(100); c.depositar(50); _res = c.saldo", 150),
        ("c = ContaBancaria(100); c.sacar(30); _res = c.saldo", 70),
        ("c = ContaBancaria(0); c.sacar(10); _res = c.saldo", 0),
        ("c = ContaBancaria(200); c.depositar(50); c.sacar(100); _res = c.saldo", 150),
    ],
    modelo=(
        "class ContaBancaria:\n"
        "    def __init__(self, saldo):\n"
        "        self.saldo = saldo\n"
        "\n"
        "    def depositar(self, valor):\n"
        "        # some valor ao saldo\n"
        "        pass\n"
        "\n"
        "    def sacar(self, valor):\n"
        "        # desconte valor SE houver saldo suficiente\n"
        "        pass"
    ),
    dica="Em `depositar`: `self.saldo = self.saldo + valor`. Em `sacar`: `if valor <= self.saldo: self.saldo = self.saldo - valor`.",
    nome_tarefa="tema14_conta_bancaria",
)

rodape_fases(__file__)
rodape_tema(__file__)
