import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o programa que inverte a palavra **arara**. A previsão da
fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t8_rodar",
    enunciado="Faça este programa imprimir `arara`.",
    esperado="arara",
    modelo='palavra = "arara"\nprint(palavra[::-1])',
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** `palavra[::-1]` não muda a variável `palavra` — ele cria
uma **nova** string invertida. Strings em Python são **imutáveis**: métodos como
`.lower()` e fatias sempre devolvem um texto novo.
"""
)

rodape_fases(__file__)
