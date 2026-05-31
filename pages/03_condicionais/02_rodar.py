import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o classificador para um aluno de **média 6** e veja a saída.
A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t3_rodar",
    enunciado="Faça este programa imprimir `Recuperação`.",
    esperado="Recuperação",
    modelo=(
        "media = 6\n"
        "if media >= 7:\n"
        '    print("Aprovado")\n'
        "elif media >= 5:\n"
        '    print("Recuperação")\n'
        "else:\n"
        '    print("Reprovado")'
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** a **indentação** (os espaços antes do `print`) não é
enfeite — é ela que diz ao Python *o que pertence a cada `if`*. Sem ela, o
programa nem roda.
"""
)
