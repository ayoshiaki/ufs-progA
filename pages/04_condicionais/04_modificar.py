import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
A escola mudou a regra: agora a aprovação exige média **≥ 6** (em vez de 7).
Ajuste o programa para um aluno de **média 6**, que agora deve ser **Aprovado**.

O programa deve imprimir:

```
Aprovado
```
"""
)

exercicio_saida_sandbox(
    chave="t4_modificar",
    enunciado="Mude o limite de aprovação para `>= 6`.",
    esperado="Aprovado",
    modelo=(
        "media = 6\n"
        "if media >= 7:\n"
        '    print("Aprovado")\n'
        "elif media >= 5:\n"
        '    print("Recuperação")\n'
        "else:\n"
        '    print("Reprovado")'
    ),
    dica="Troque o `7` da primeira condição por `6`.",
)

rodape_fases(__file__)
