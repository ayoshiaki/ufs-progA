import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Confirme sua previsão: este programa deve imprimir `60`.")

exercicio_saida(
    chave="t5_rodar",
    enunciado="Rode o acumulador de soma.",
    esperado="60",
    modelo="soma = 0\nfor n in [10, 20, 30]:\n    soma = soma + n\nprint(soma)",
    dica="É só rodar. Observe como `soma` muda a cada volta.",
)

st.info(
    "🔑 Padrão do **acumulador**: criar uma variável *antes* do laço (aqui `soma = 0`) "
    "e atualizá-la *dentro* do laço. Você vai reusar isso a vida toda."
)

st.divider()
st.markdown(
    """
Agora um **`while`**: uma contagem regressiva que repete **enquanto**
`contador > 0`. Deve imprimir os números 5 a 1, um por linha, e depois `Fim!`.
"""
)

exercicio_saida(
    chave="t5_rodar_while",
    enunciado="Rode a contagem regressiva com `while`.",
    esperado="5\n4\n3\n2\n1\nFim!",
    modelo=(
        "contador = 5\n"
        "while contador > 0:\n"
        "    print(contador)\n"
        "    contador = contador - 1\n"
        'print("Fim!")'
    ),
    dica="É só rodar. Repare que `contador = contador - 1` é o que faz a condição "
         "`contador > 0` um dia ficar falsa — sem essa linha, seria um laço infinito.",
)

rodape_fases(__file__)
