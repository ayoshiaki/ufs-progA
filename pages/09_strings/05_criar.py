import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. O `texto` **já existe** — guarde em `_res` `True` se
ele for um palíndromo e `False` caso contrário.

A verificação deve **ignorar maiúsculas/minúsculas e espaços** — assim
`"Ame a ema"` conta como palíndromo.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t9_criar",
    enunciado="Verifique se `texto` é palíndromo e guarde em `_res`:",
    casos=[
        ({"texto": "arara"}, True),
        ({"texto": "casa"}, False),
        ({"texto": "Ame a ema"}, True),
        ({"texto": "Python"}, False),
        ({"texto": "ovo"}, True),
    ],
    modelo=(
        "# o texto esta na variavel texto.\n"
        "# 1) deixe minusculo  2) tire os espacos  3) compare com o invertido\n"
        "_res = False"
    ),
    dica='Tire espacos com `texto.replace(" ", "")`, use `.lower()`, e compare com `texto[::-1]`. Guarde em `_res`.',
    nome_tarefa="tema9_eh_palindromo",
)

rodape_fases(__file__)
rodape_tema(__file__)
