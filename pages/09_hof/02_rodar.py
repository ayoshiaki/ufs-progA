import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o programa que define `aplicar` e o chama passando a função
`quadrado`. A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t9_rodar",
    enunciado="Faça este programa imprimir `16`.",
    esperado="16",
    modelo=(
        "def aplicar(f, x):\n"
        "    return f(x)\n"
        "\n"
        "def quadrado(n):\n"
        "    return n * n\n"
        "\n"
        "print(aplicar(quadrado, 4))"
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** repare que `quadrado` é passado **sem parênteses** —
`aplicar(quadrado, 4)`, não `aplicar(quadrado(), 4)`. Com parênteses você
*chamaria* a função; sem eles, você *entrega a própria função* para `aplicar`
chamar lá dentro.
"""
)

rodape_fases(__file__)
