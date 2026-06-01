import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

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

st.caption(
    "📖 **Documentação oficial do Python:** [Estruturas de dados — listas, tuplas e dicionários](https://docs.python.org/pt-br/3/tutorial/datastructures.html)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
