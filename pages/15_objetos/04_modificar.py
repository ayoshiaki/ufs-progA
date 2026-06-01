import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
A conta só sabe depositar. **Adicione um método** `sacar(valor)` que **só
desconta se houver saldo suficiente** (senão, não faz nada).

Para uma conta com 100, sacando 30, o programa deve imprimir:

```
70
```
"""
)

exercicio_saida_sandbox(
    chave="t15_modificar",
    enunciado="Adicione o método `sacar` (com a verificação de saldo).",
    esperado="70",
    modelo=(
        "class ContaBancaria:\n"
        "    def __init__(self, saldo):\n"
        "        self.saldo = saldo\n"
        "\n"
        "    def depositar(self, valor):\n"
        "        self.saldo = self.saldo + valor\n"
        "\n"
        "    # crie aqui o metodo sacar(self, valor)\n"
        "\n"
        "c = ContaBancaria(100)\n"
        "c.sacar(30)\n"
        "print(c.saldo)"
    ),
    dica="No corpo do método: `if valor <= self.saldo:` e dentro `self.saldo = self.saldo - valor`.",
)

rodape_fases(__file__)
