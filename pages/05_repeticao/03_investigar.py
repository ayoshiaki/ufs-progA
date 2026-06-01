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

st.divider()
st.markdown("Agora **`for` vs `while`** — escolher o laço certo para cada situação.")

stb.single_choice(
    "Em qual situação o `while` é a melhor escolha?",
    [
        "Percorrer cada nome de uma lista já pronta.",
        "Repetir até o usuário digitar a senha certa — sem saber quantas tentativas serão.",
        "Imprimir os números de 0 a 9.",
        "Somar todos os itens de uma lista de preços.",
    ],
    1,
    success="Isso! Quando você não sabe quantas voltas serão (repete ATÉ algo mudar), o `while` brilha.",
    error="`for` serve quando você sabe o que percorrer ou quantas vezes. O `while` é para repetir ATÉ uma condição mudar (nº de voltas desconhecido).",
)

st.divider()

stb.single_choice(
    "O que costuma causar um **laço infinito** num `while`?",
    [
        "Esquecer de atualizar a variável da condição, que então nunca fica falsa.",
        "Usar `print` dentro do laço.",
        "Inicializar a variável antes do laço.",
        "Comparar com `>` em vez de `>=`.",
    ],
    0,
    success="Exato! Sem o passo que atualiza a variável, a condição fica sempre verdadeira e o laço nunca termina.",
    error="O laço infinito vem de a condição nunca virar falsa — normalmente porque a variável testada não é atualizada dentro do laço.",
)

rodape_fases(__file__)
