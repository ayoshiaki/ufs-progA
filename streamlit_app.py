"""
Programação A — livro interativo.

Rode com:
    streamlit run streamlit_app.py
"""

import streamlit as st
import streamlit_book as stb
from pathlib import Path

# Workaround para um bug do streamlit_book 0.7.6: em chapter_config.py a função
# é definida como `get_query()` mas chamada como `get_query_params()`, causando
# `NameError` com versões recentes do Streamlit. Criamos o alias que falta.
# A guarda `hasattr` torna o patch inócuo quando o upstream corrigir o nome.
import streamlit_book.chapter_config as _chapter_config
if not hasattr(_chapter_config, "get_query_params"):
    _chapter_config.get_query_params = _chapter_config.get_query

st.set_page_config(
    page_title="Programação A",
    page_icon="🐍",
    layout="centered",
)

current = Path(__file__).parent / "pages"

stb.set_book_config(
    menu_title="Programação A",
    menu_icon="terminal",
    options=[
        "Boas-vindas",
        "1 · Pensamento computacional",
        "2 · Tipos e expressões",
        "3 · Condicionais",
        "4 · Repetição",
        "5 · Listas, tuplas e dicionários",
        "6 · Strings",
        "7 · Funções",
        "8 · Arquivos e erros",
        "9 · Introdução a objetos",
        "10 · OO: herança e polimorfismo",
    ],
    paths=[
        current / "00_boas_vindas.py",
        current / "01_pensamento_computacional",
        current / "02_tipos",
        current / "03_condicionais",
        current / "04_repeticao",
        current / "05_colecoes",
        current / "06_strings",
        current / "07_funcoes",
        current / "08_arquivos_erros",
        current / "09_objetos",
        current / "10_heranca",
    ],
    icons=[
        "house", "lightbulb", "calculator", "signpost-split", "arrow-repeat",
        "list-ul", "fonts", "box", "file-earmark", "diagram-3", "diagram-3-fill",
    ],
    save_answers=True,
    # Esconde a legenda "Page X of Y. File: <caminho>" (vazava o caminho do
    # arquivo na tela) e destaca o capítulo ativo no menu lateral.
    display_page_info=False,
    styles={
        "container": {"padding": "0.5rem 0.3rem"},
        "icon": {"font-size": "0.95rem"},
        "nav-link": {
            "font-size": "0.92rem",
            "padding": "0.45rem 0.6rem",
            "margin": "0.12rem 0",
            "border-radius": "8px",
        },
        "nav-link-selected": {"background-color": "#ff4b4b", "font-weight": "600"},
    },
)
