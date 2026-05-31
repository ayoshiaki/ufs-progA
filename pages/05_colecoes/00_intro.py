import streamlit as st

st.title("Tema 5 · Listas, tuplas e dicionários")
st.subheader("Fase 0 — Aquecimento")

st.markdown(
    """
**O problema do tema:** montar uma **agenda de contatos** que guarda o telefone
de cada pessoa e permite buscar pelo nome.

Guardar *vários* valores juntos pede uma **estrutura de dados**:

- **lista** — sequência ordenada, acessada por posição: `nomes[0]`
- **tupla** — como a lista, mas **imutável** (não muda depois de criada)
- **dicionário** — pares **chave → valor**, acessado pela chave: `agenda["Ana"]`

Para uma agenda, o dicionário é perfeito: a **chave** é o nome e o **valor** é
o telefone.

> 💭 **Pense antes de avançar:** numa lista você acha um item pela *posição*
> (0, 1, 2…). Num dicionário, você acha pelo *nome*. Qual faz mais sentido para
> "qual o telefone da Ana?"
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
