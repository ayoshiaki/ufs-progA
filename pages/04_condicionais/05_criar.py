import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. A nota **já está** na variável `media` — guarde em
`_res` o texto certo:

- `"Aprovado"` se a média for **≥ 7**
- `"Recuperação"` se for **≥ 5** (e menor que 7)
- `"Reprovado"` caso contrário

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t4_criar",
    enunciado="Use `if / elif / else` e guarde o texto em `_res`:",
    casos=[
        ({"media": 8}, "Aprovado"),
        ({"media": 7}, "Aprovado"),
        ({"media": 6}, "Recuperação"),
        ({"media": 5}, "Recuperação"),
        ({"media": 4.5}, "Reprovado"),
        ({"media": 3}, "Reprovado"),
    ],
    modelo=(
        "# a nota esta na variavel media.\n"
        "# Use if / elif / else e guarde o texto em _res.\n"
        '_res = "Reprovado"'
    ),
    dica='Atencao aos acentos: o texto e exatamente "Recuperacao" com cedilha e til -> "Recuperação". Guarde em `_res`, nao use print.',
    nome_tarefa="tema4_situacao",
)

rodape_fases(__file__)
rodape_tema(__file__)
