import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)

stb.single_choice(
    "Por que `soma = 0` precisa estar ANTES do laço, e não dentro dele?",
    [
        "Por estilo; tanto faz onde colocar.",
        "Se estivesse dentro, `soma` voltaria a 0 a cada volta e o total seria perdido.",
        "Porque o laço não aceita variáveis dentro.",
        "Para o programa rodar mais rápido.",
    ],
    1,
    success="Exato! Inicializar dentro do laço zeraria o acumulador a cada iteração.",
    error="Imagine `soma = 0` repetindo a cada volta. O que aconteceria com o total?",
)

st.divider()

stb.multiple_choice(
    "Para calcular a MÉDIA de uma lista de notas, do que você precisa?",
    {
        "Acumular a soma das notas num laço.": True,
        "Saber quantas notas existem (a quantidade).": True,
        "Dividir a soma pela quantidade no final.": True,
        "Ordenar as notas antes de somar.": False,
    },
    success="Perfeito — soma ÷ quantidade. Ordenar é irrelevante para a média.",
    error="Média = soma de tudo dividida pela quantidade. Ordenar muda algo?",
)

rodape_fases(__file__)
