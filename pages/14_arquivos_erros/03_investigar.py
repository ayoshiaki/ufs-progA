import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em quando e como tratar erros.")

stb.single_choice(
    "Por que usar `except ValueError` em vez de um `except` que pega qualquer erro?",
    [
        "Porque é mais bonito.",
        "Para silenciar só o erro esperado e não esconder bugs de verdade.",
        "Porque `ValueError` é o único erro que existe.",
        "Não há diferença.",
    ],
    1,
    success="Isso! Capturar um tipo específico evita engolir erros que você não previu (e que indicariam um bug real).",
    error="Capturar só `ValueError` trata o caso esperado (texto que não é número) sem mascarar outros erros.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre arquivos e erros estão corretas?",
    {
        "`with open(...)` fecha o arquivo automaticamente no fim do bloco.": True,
        "`float(\"abc\")` lança `ValueError`.": True,
        "`try/except` evita que um dado inválido derrube o programa todo.": True,
        "Abrir um arquivo que não existe sempre devolve uma string vazia.": False,
    },
    success="Mandou bem! `with` cuida do fechamento, `float` de texto inválido dá `ValueError`, e o `try/except` te protege — mas arquivo inexistente lança `FileNotFoundError`, não string vazia.",
    error="Revise: o que acontece ao abrir um arquivo que não existe? (Erro `FileNotFoundError`, não string vazia.)",
)

rodape_fases(__file__)
