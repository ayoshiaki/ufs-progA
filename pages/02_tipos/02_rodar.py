import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o programa que converte **20 °C** para Fahrenheit e veja a
saída. A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t2_rodar",
    enunciado="Faça este programa imprimir `68.0`.",
    esperado="68.0",
    modelo="c = 20\nf = c * 9 / 5 + 32\nprint(f)",
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** mesmo que o resultado "pareça" inteiro (68), a divisão `/`
faz o Python guardar um `float` (`68.0`). O **tipo** do valor importa tanto
quanto o valor.
"""
)
