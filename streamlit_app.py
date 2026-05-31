"""
Programação A — livro interativo.

Rode com:
    streamlit run streamlit_app.py
"""

import streamlit as st
import streamlit_book as stb
from pathlib import Path

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
)
