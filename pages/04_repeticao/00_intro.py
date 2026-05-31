import streamlit as st

st.title("Tema 4 · Repetição")
st.subheader("Fase 0 — Aquecimento")

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
