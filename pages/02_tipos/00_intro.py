import streamlit as st

st.title("Tema 2 · Tipos e expressões")
st.subheader("Fase 0 — Aquecimento")

st.markdown(
    """
**O problema do tema:** um aplicativo de viagem precisa converter a temperatura
de **Celsius para Fahrenheit** para mostrar ao turista.

A fórmula é conhecida: `F = C × 9/5 + 32`. Mas para o computador acertar a
conta, três ideias entram em jogo:

- **Tipos** — `int` (inteiro), `float` (com casas decimais) e `str` (texto)
- **Operadores** — `+`, `-`, `*`, `/` e a diferença entre `/` e `//`
- **Conversão** — misturar `int` e `float` muda o tipo do resultado

> 💭 **Pense antes de avançar:** quanto é `9/5` em Python? E `9//5`? Um desses
> resultados tem casas decimais e o outro não — essa diferença é o coração
> deste tema.
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
