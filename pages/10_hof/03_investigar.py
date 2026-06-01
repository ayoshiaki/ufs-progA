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
        "`lambda x: x + 1` é uma função sem nome.": True,
        "Passar `quadrado` (sem parênteses) entrega a função; `quadrado()` a chamaria.": True,
        "Uma `lambda` só pode ter um parâmetro.": False,
    },
    success="Mandou bem! Funções são valores, `lambda` é função anônima, e sem parênteses você passa a função em si.",
    error="Revise: funções podem ser passadas adiante; `lambda` pode ter vários parâmetros; sem `()` você passa a função, não o resultado.",
)

rodape_fases(__file__)
