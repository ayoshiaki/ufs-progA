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

from utils.progresso import salvar_progresso

# Suprime o aviso de "save answers" embutido no streamlit_book (caixa amarela em
# inglês, com um link relativo `?token=...` incompleto). Definir a flag ANTES de
# `set_book_config` faz o livro pular esse aviso; o token continua sendo criado.
# Em seu lugar mostramos `salvar_progresso()` na barra lateral — em português e
# com a URL completa. Ver utils/progresso.py.
st.session_state["warned_about_save_answers"] = True

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
        "8 · Funções de ordem superior",
        "9 · Arquivos e erros",
        "10 · Introdução a objetos",
        "11 · OO: herança e polimorfismo",
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
        current / "08_hof",
        current / "09_arquivos_erros",
        current / "10_objetos",
        current / "11_heranca",
    ],
    icons=[
        "house", "lightbulb", "calculator", "signpost-split", "arrow-repeat",
        "list-ul", "fonts", "box", "arrow-right-circle", "file-earmark",
        "diagram-3", "diagram-3-fill",
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

# Nosso cartão "Salvar progresso" na barra lateral (substitui o aviso embutido).
salvar_progresso()
