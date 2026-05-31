import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `situacao(media)` que
**devolva** (com `return`) o texto certo:

- `"Aprovado"` se a média for **≥ 7**
- `"Recuperação"` se for **≥ 5** (e menor que 7)
- `"Reprovado"` caso contrário

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t3_criar",
    enunciado="Implemente a função `situacao`:",
    func_name="situacao",
    cases=[
        ((8,), "Aprovado"), ((7,), "Aprovado"), ((6,), "Recuperação"),
        ((5,), "Recuperação"), ((4.5,), "Reprovado"), ((3,), "Reprovado"),
    ],
    modelo=(
        "def situacao(media):\n"
        "    # use if / elif / else e return\n"
        '    return "Reprovado"'
    ),
    dica='Atencao aos acentos: o texto e exatamente "Recuperacao" com cedilha e til -> "Recuperação". Use `return`, nao `print`.',
    nome_tarefa="tema3_situacao",
)

rodape_fases(__file__)
rodape_tema(__file__)
