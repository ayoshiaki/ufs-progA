import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `eh_palindromo(texto)` que
**devolva** (com `return`) `True` se o texto for um palíndromo e `False` caso
contrário.

A verificação deve **ignorar maiúsculas/minúsculas e espaços** — assim
`"Ame a ema"` conta como palíndromo.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t7_criar",
    enunciado="Implemente a função `eh_palindromo`:",
    func_name="eh_palindromo",
    cases=[
        (("arara",), True), (("casa",), False), (("Ame a ema",), True),
        (("Python",), False), (("ovo",), True),
    ],
    modelo=(
        "def eh_palindromo(texto):\n"
        "    # 1) deixe minusculo  2) tire os espacos  3) compare com o invertido\n"
        "    return False"
    ),
    dica='Tire espacos com `texto.replace(" ", "")`, use `.lower()`, e compare com `texto[::-1]`.',
    nome_tarefa="tema7_eh_palindromo",
)

rodape_fases(__file__)
rodape_tema(__file__)
