import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Esta `ContaBancaria` está **sem proteção**: o `sacar` desconta sem checar o
saldo, então a conta fica **negativa**. **Conserte** o `sacar` para só descontar
quando houver saldo suficiente.

Para a conta abaixo (saldo 50, tentando sacar 80), o saque deve ser **barrado**
e o programa deve imprimir:

```
50
```
"""
)

exercicio_saida_sandbox(
    chave="t16_modificar",
    enunciado="Faça o `sacar` checar o saldo antes de descontar.",
    esperado="50",
    modelo=(
        "class ContaBancaria:\n"
        "    def __init__(self, saldo):\n"
        "        self._saldo = saldo\n"
        "\n"
        "    @property\n"
        "    def saldo(self):\n"
        "        return self._saldo\n"
        "\n"
        "    def sacar(self, valor):\n"
        "        self._saldo -= valor      # <- desconta SEM checar o saldo\n"
        "\n"
        "c = ContaBancaria(50)\n"
        "c.sacar(80)\n"
        "print(c.saldo)"
    ),
    dica="Proteja a regra no método: `if 0 < valor <= self._saldo: self._saldo -= valor`.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** a regra "não sacar mais do que tem" pertence à **classe**,
não a quem usa a conta. Encapsulada, a regra vale sempre — não importa quem chame
o `sacar`.
"""
)

rodape_fases(__file__)
