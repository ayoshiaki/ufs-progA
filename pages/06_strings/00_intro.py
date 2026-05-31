import streamlit as st

st.title("Tema 6 · Strings")
st.subheader("Fase 0 — Aquecimento")

st.markdown(
    """
**O problema do tema:** validar e formatar textos — por exemplo, descobrir se
uma palavra é um **palíndromo** (lê-se igual de trás para frente, como *arara*).

Texto, em programação, é uma **string** (`str`). E strings têm superpoderes:

- **indexação e fatiamento** — `texto[0]`, `texto[::-1]` (inverte!)
- **métodos** — `.lower()`, `.upper()`, `.strip()`, `.replace()`, `.split()`
- **tamanho** — `len(texto)`

> 💭 **Pense antes de avançar:** "Arara" começa com A maiúsculo e "arara"
> com minúsculo. Para o computador, esses dois textos são *iguais*? Se não,
> como fazer a comparação ignorar maiúsculas/minúsculas?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
