import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode a agenda e busque o telefone da **Ana**. A previsão da fase
anterior estava certa?
"""
)

exercicio_saida_sandbox(
    chave="t6_rodar",
    enunciado="Faça este programa imprimir `99991111`.",
    esperado="99991111",
    modelo=(
        'agenda = {"Ana": "99991111", "Bia": "98882222"}\n'
        'print(agenda["Ana"])'
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** buscar uma chave que **não existe** com `agenda["Zé"]`
quebraria o programa (`KeyError`). Por isso, mais à frente, vamos usar o método
`.get()`, que devolve um valor padrão em vez de dar erro.
"""
)

rodape_fases(__file__)
