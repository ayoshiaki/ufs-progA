import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Cole o código abaixo (ou digite) e clique em **Rodar e verificar**.
A previsão da fase anterior estava certa?
"""
)

exercicio_saida_sandbox(
    chave="t1_rodar",
    enunciado="Faça este programa imprimir `Total: 15`.",
    esperado="Total: 15",
    modelo='preco = 5\nquantidade = 3\ntotal = preco * quantidade\nprint("Total:", total)',
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** o computador executa **uma linha por vez, de cima para
baixo**. A variável `total` só existe *depois* da linha que a cria. Trocar a
ordem das linhas quebraria o programa — guarde essa ideia para a fase Investigar.
"""
)

rodape_fases(__file__)
