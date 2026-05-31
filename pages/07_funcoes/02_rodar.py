import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o programa que define `dobro` e chama com `5`. A previsão da
fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t7_rodar",
    enunciado="Faça este programa imprimir `10`.",
    esperado="10",
    modelo="def dobro(x):\n    return x * 2\n\nprint(dobro(5))",
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** a função `dobro` só *executa* quando é **chamada**
(`dobro(5)`). Definir (`def`) é como escrever a receita; chamar é cozinhar. Você
pode chamar quantas vezes quiser, com valores diferentes.
"""
)
