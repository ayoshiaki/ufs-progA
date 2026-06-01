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
    chave="t11_rodar",
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

st.divider()
st.markdown(
    """
Agora o **outro lado**: rode uma função que **devolve** outra função. A `dobro`
nem aparece escrita à mão — ela é fabricada por `multiplicador(2)`.
"""
)

exercicio_saida(
    chave="t11_rodar_fabrica",
    enunciado="Faça este programa imprimir `10`.",
    esperado="10",
    modelo=(
        "def multiplicador(n):\n"
        "    def multiplica(x):\n"
        "        return x * n\n"
        "    return multiplica\n"
        "\n"
        "dobro = multiplicador(2)\n"
        "print(dobro(5))"
    ),
    dica="Já está pronto — é só rodar. `multiplicador(2)` fabrica a função guardada em `dobro`.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** a chamada acontece em **dois passos**. Primeiro
`multiplicador(2)` devolve uma função; depois você chama essa função com `(5)`.
Dá até para juntar tudo numa linha: `multiplicador(2)(5)` também vale `10`.
"""
)

rodape_fases(__file__)
