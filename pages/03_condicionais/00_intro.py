import streamlit as st

st.title("Tema 3 · Condicionais")
st.subheader("Fase 0 — Aquecimento")

st.markdown(
    """
**O problema do tema:** a secretaria precisa de um programa que, a partir da
**média** de um aluno, diga a situação dele:

- média **≥ 7** → **Aprovado**
- média entre **5 e 7** → **Recuperação**
- média **< 5** → **Reprovado**

O programa precisa **tomar decisões**. Para isso usamos:

- **`if`** — faz algo *se* uma condição for verdadeira
- **`elif`** — testa outra condição *se* a anterior falhou
- **`else`** — o que fazer quando *nenhuma* condição bateu
- **comparações** — `>=`, `<`, `==`, que devolvem `True` ou `False`

> 💭 **Pense antes de avançar:** a ordem dos testes importa? Se você checasse
> `media >= 5` antes de `media >= 7`, o que aconteceria com um aluno de média 9?
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
