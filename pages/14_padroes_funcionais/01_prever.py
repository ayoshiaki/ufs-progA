import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia cada código **sem rodar** e responda. Confirmamos na próxima fase.")

st.code(
    '''acoes = {
    "dobrar":   lambda x: x * 2,
    "negar":    lambda x: -x,
    "quadrado": lambda x: x * x,
}

print(acoes["quadrado"](5))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    ["25", "10", "-5", "Erro: dict não é chamável"],
    0,
    success="Isso! `acoes[\"quadrado\"]` devolve a função `lambda x: x * x`; aplicada a 5 dá 25.",
    error="A chave `\"quadrado\"` seleciona a função `lambda x: x * x`. Chamando-a com 5: 5 * 5 = 25.",
)

st.divider()

st.code(
    '''from functools import partial

def soma(a, b):
    return a + b

soma10 = partial(soma, 10)
print(soma10(5))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    ["15", "10", "5", "Uma função, não um número"],
    0,
    success="Isso! `partial(soma, 10)` fixa `a=10`; ao chamar `soma10(5)`, `b=5` e a soma é 15.",
    error="`partial(soma, 10)` deixa o `10` no lugar de `a`. `soma10(5)` completa com `b=5`: 10 + 5 = 15.",
)

st.divider()

st.code(
    '''def descrever(ponto):
    match ponto:
        case (0, 0):  return "origem"
        case (x, 0):  return f"eixo X em {x}"
        case (0, y):  return f"eixo Y em {y}"
        case (x, y):  return f"({x}, {y})"

print(descrever((0, 7)))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    ["eixo Y em 7", "origem", "eixo X em 7", "(0, 7)"],
    0,
    success="Isso! `(0, 7)` não casa com `(0, 0)` nem `(x, 0)`, mas casa com `(0, y)` (y = 7).",
    error="O `match` testa os casos em ordem: `(0, 7)` bate no padrão `(0, y)`, ligando `y = 7`.",
)

rodape_fases(__file__)
