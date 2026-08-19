import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_expressoes_sandbox
from utils.navegacao import cabecalho, rodape_tema, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Hora de resolver sozinho, juntando dois padrões. Implemente:

1. **`pipe(valor, *funcs)`** — aplica as funções **na ordem em que aparecem** e
   devolve o resultado final. Sem nenhuma função, devolve o próprio `valor`.
2. **`calcular(op, a, b)`** — usa uma **tabela de despacho** (um `dict`) para
   escolher a operação pelo nome: `"somar"`, `"subtrair"` e `"multiplicar"`.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_expressoes_sandbox(
    chave="t14_criar",
    enunciado="Implemente `pipe` e `calcular`:",
    cases=[
        ("_res = pipe(3, lambda x: x + 1, lambda x: x * 2)", 8),
        ("_res = pipe(10)", 10),
        ("_res = calcular('somar', 2, 3)", 5),
        ("_res = calcular('subtrair', 10, 4)", 6),
        ("_res = calcular('multiplicar', 4, 5)", 20),
    ],
    modelo=(
        "def pipe(valor, *funcs):\n"
        "    # aplique cada função de funcs, na ordem, sobre 'valor'\n"
        "    return valor\n"
        "\n"
        "def calcular(op, a, b):\n"
        "    # monte um dict op -> função e use-o para escolher a operação\n"
        "    tabela = {\n"
        "        # \"somar\": lambda a, b: a + b,\n"
        "        # ...\n"
        "    }\n"
        "    return None"
    ),
    dica=(
        "Em `pipe`: `for f in funcs: valor = f(valor)` e depois `return valor`. "
        "Em `calcular`: monte `tabela = {\"somar\": lambda a, b: a + b, "
        "\"subtrair\": lambda a, b: a - b, \"multiplicar\": lambda a, b: a * b}` "
        "e devolva `tabela[op](a, b)`."
    ),
    nome_tarefa="tema14_padroes_funcionais",
)

rodape_fases(__file__)
rodape_tema(__file__)
