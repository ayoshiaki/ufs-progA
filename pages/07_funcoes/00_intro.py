import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro

cabecalho_intro(__file__)

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
