import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode o programa que soma as notas válidas, ignorando o `"x"`.
A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t8_rodar",
    enunciado="Faça este programa imprimir `16.0`.",
    esperado="16.0",
    modelo=(
        'valores = ["7", "x", "9"]\n'
        "soma = 0\n"
        "for v in valores:\n"
        "    try:\n"
        "        soma = soma + float(v)\n"
        "    except ValueError:\n"
        "        pass\n"
        "print(soma)"
    ),
    dica="Já está pronto no modelo — é só rodar para confirmar sua previsão.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** o `except ValueError` só captura *esse* tipo de erro. Um
problema diferente (por exemplo, um nome de variável errado) **não** seria
silenciado — e isso é bom: você só ignora o erro que sabe tratar.
"""
)
