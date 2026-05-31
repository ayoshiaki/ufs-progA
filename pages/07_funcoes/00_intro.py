import streamlit as st

st.title("Tema 7 · Funções")
st.subheader("Fase 0 — Aquecimento")

st.markdown(
    """
**O problema do tema:** um programa de loja repete o mesmo cálculo de total em
vários lugares. Quando a regra muda, é preciso corrigir em todos eles — fácil
esquecer um. A solução é **dar um nome ao cálculo**: criar uma **função**.

Uma função é um bloco reutilizável que:

- recebe **parâmetros** (entradas): `def total(preco, qtd, desconto):`
- faz um processamento
- **devolve** um resultado com `return`

Escreve-se uma vez, usa-se em qualquer lugar — e a regra fica num ponto só.

> 💭 **Pense antes de avançar:** qual a diferença entre `print(x)` e
> `return x` dentro de uma função? Uma mostra na tela; a outra **entrega** o
> valor para quem chamou — e só com `return` dá para usar o resultado em outra
> conta.
"""
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")
