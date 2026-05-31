import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** dada uma lista de notas, calcular a **média** da turma.

Você *poderia* somar nota por nota na mão... mas e se a turma tiver 300 alunos?
A ideia central aqui é a **repetição**: dar a mesma instrução muitas vezes sem
reescrevê-la. Em Python, o laço `for` percorre cada item de uma coleção.

> 💭 **Pense antes de avançar:** para tirar a média você precisa de duas coisas
> que vão *mudando* a cada volta do laço. Quais são?
"""
)

rodape_fases(__file__)
