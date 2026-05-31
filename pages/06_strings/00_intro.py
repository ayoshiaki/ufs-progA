import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

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

rodape_fases(__file__)
