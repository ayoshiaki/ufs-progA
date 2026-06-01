import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva a `ContaBancaria` **encapsulada**:

- guarde o saldo em `self._saldo` (interno);
- exponha `saldo` como **`@property`** (só leitura — `c.saldo` lê, `c.saldo = x`
  deve dar erro);
- `depositar(valor)` — soma **só se `valor > 0`**;
- `sacar(valor)` — desconta **só se houver saldo suficiente** (`0 < valor <= saldo`).

Os testes conferem o saldo após operações válidas e inválidas, e que o saldo
**não** pode ser alterado direto. O código roda numa **sandbox no seu navegador**
(WebAssembly). Passe em todos para liberar o comprovante de entrega.
"""
)

exercicio_expressoes_sandbox(
    chave="t16_criar",
    enunciado="Implemente a `ContaBancaria` encapsulada:",
    cases=[
        ("c = ContaBancaria(100); c.depositar(50); _res = c.saldo", 150),
        ("c = ContaBancaria(100); c.sacar(30); _res = c.saldo", 70),
        ("c = ContaBancaria(100); c.sacar(999); _res = c.saldo", 100),
        ("c = ContaBancaria(100); c.depositar(-50); _res = c.saldo", 100),
        ("c = ContaBancaria(100)\ntry:\n    c.saldo = 5\n    _res = 'mudou'\nexcept Exception:\n    _res = 'protegido'", "protegido"),
    ],
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
        "        # some SE valor > 0\n"
        "        pass\n"
        "\n"
        "    def sacar(self, valor):\n"
        "        # desconte SE 0 < valor <= self._saldo\n"
        "        pass"
    ),
    dica="Em `depositar`: `if valor > 0: self._saldo += valor`. Em `sacar`: "
         "`if 0 < valor <= self._saldo: self._saldo -= valor`. Não crie um setter "
         "para `saldo` — assim `c.saldo = x` continua barrado.",
    nome_tarefa="tema16_conta_encapsulada",
)

rodape_fases(__file__)
rodape_tema(__file__)
