import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em funções como valores que se passam adiante.")

stb.single_choice(
    "Por que passar a função como argumento, em vez de copiar o laço e trocar só a operação?",
    [
        "Porque copiar o laço é proibido em Python.",
        "Porque assim o mesmo código serve para QUALQUER ação — é só trocar a função passada.",
        "Porque funções passadas como argumento rodam mais rápido.",
        "Não há diferença; é só estilo.",
    ],
    1,
    success="Isso! A estrutura fica num lugar só; a ação vira um parâmetro. Menos repetição, menos erro.",
    error="A vantagem é reúso: a estrutura (o laço/chamada) fica fixa e a AÇÃO chega como argumento.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações estão corretas?",
    {
        "Uma função pode ser passada como argumento para outra função.": True,
        "Uma função pode devolver outra função (com `return`).": True,
        "`lambda x: x + 1` é uma função sem nome.": True,
        "Em `multiplicador(n)`, a função interna lembra o valor de `n` (fechamento).": True,
        "Passar `quadrado` (sem parênteses) entrega a função; `quadrado()` a chamaria.": True,
        "Uma `lambda` só pode ter um parâmetro.": False,
    },
    success="Mandou bem! Funções são valores: dá para passá-las adiante E devolvê-las; a função devolvida lembra o que capturou.",
    error="Revise: funções podem ser passadas E devolvidas; `lambda` pode ter vários parâmetros; sem `()` você passa a função, não o resultado.",
)

st.divider()

stb.single_choice(
    "Por que querer uma função que DEVOLVE outra função, como `multiplicador(n)`?",
    [
        "Para configurar a função UMA vez (fixar o `n`) e reusar a função pronta com vários valores.",
        "Porque é a única forma de uma função ter mais de um parâmetro.",
        "Porque funções internas rodam mais rápido que `lambda`.",
        "Não há motivo prático; é só para complicar.",
    ],
    0,
    success="Isso! Você fixa o `n` uma vez e ganha uma função especializada (`dobro`, `triplo`...) para reusar quantas vezes quiser.",
    error="A ideia é especializar: fixa-se o `n` uma vez e a função devolvida já vem pronta para reusar com qualquer valor.",
)

rodape_fases(__file__)
