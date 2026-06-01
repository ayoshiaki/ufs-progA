import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o `fatorial` recursivo com `5`. A previsão da fase anterior
estava certa?
"""
)

exercicio_saida_sandbox(
    chave="t11_rodar",
    enunciado="Faça este programa imprimir `120`.",
    esperado="120",
    modelo=(
        "def fatorial(n):\n"
        "    if n == 0:\n"
        "        return 1\n"
        "    return n * fatorial(n - 1)\n"
        "\n"
        "print(fatorial(5))"
    ),
    dica="Ja esta pronto no modelo — e so rodar para confirmar sua previsao.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** cada chamada de `fatorial` fica *esperando* o resultado de
uma chamada menor (`fatorial(5)` espera `fatorial(4)`, que espera `fatorial(3)`…).
Quando o caso base (`n == 0`) devolve `1`, os resultados voltam multiplicando-se
de volta até o topo. É essa pilha de chamadas que faz a recursão funcionar.
"""
)

rodape_fases(__file__)
