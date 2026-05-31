import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_funcao_sandbox

st.subheader("Fase 5 — 🛠️ Criar (entrega)")
st.markdown(
    """
Hora de resolver sozinho. Escreva uma **função** `celsius_para_fahrenheit(c)`
que receba uma temperatura em Celsius e **devolva** (com `return`) o valor em
Fahrenheit.

O código roda numa **sandbox no seu navegador** (WebAssembly) — nada é executado
no servidor. Feche todos os testes para liberar o comprovante de entrega.
"""
)

exercicio_funcao_sandbox(
    chave="t2_criar",
    enunciado="Implemente a função `celsius_para_fahrenheit`:",
    func_name="celsius_para_fahrenheit",
    cases=[((0,), 32.0), ((100,), 212.0), ((20,), 68.0), ((-40,), -40.0), ((25,), 77.0)],
    modelo="def celsius_para_fahrenheit(c):\n    # seu codigo aqui\n    return 0",
    dica="A formula e `c * 9 / 5 + 32`. Use `return` (nao `print`).",
    nome_tarefa="tema2_celsius_fahrenheit",
)
