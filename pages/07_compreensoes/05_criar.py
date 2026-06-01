import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_script_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho. A lista `numeros` **já existe** — monte em `_res`, com
**uma compreensão de lista**, os **quadrados dos números pares** de `numeros`.

Por exemplo, para `[1, 2, 3, 4]` o resultado é `[4, 16]` (só 2 e 4 são pares;
seus quadrados são 4 e 16).

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_script_sandbox(
    chave="t7_criar",
    enunciado="Monte em `_res` a lista dos quadrados dos pares de `numeros`:",
    casos=[
        ({"numeros": [1, 2, 3, 4]}, [4, 16]),
        ({"numeros": [5, 6, 7, 8]}, [36, 64]),
        ({"numeros": [1, 3, 5]}, []),
        ({"numeros": [2]}, [4]),
        ({"numeros": []}, []),
    ],
    modelo=(
        "# a lista esta na variavel numeros.\n"
        "# Use UMA compreensao de lista com filtro e guarde em _res.\n"
        "_res = []"
    ),
    dica="Junte transformacao e filtro: `_res = [n * n for n in numeros if n % 2 == 0]`.",
    nome_tarefa="tema7_quadrados_pares",
)

rodape_fases(__file__)
rodape_tema(__file__)
