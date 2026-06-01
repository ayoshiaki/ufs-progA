import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense na compreensão como um laço que **constrói uma coleção**.")

stb.single_choice(
    "Qual a diferença entre `[x for x in dados]` e `{x for x in dados}`?",
    [
        "Colchetes constroem uma lista (mantém ordem e repetições); chaves constroem um conjunto (únicos, sem ordem).",
        "Nenhuma — colchetes e chaves são intercambiáveis.",
        "Chaves só funcionam com números; colchetes, com qualquer coisa.",
        "Colchetes criam um conjunto e chaves criam uma lista.",
    ],
    0,
    success="Isso! `[]` → lista; `{}` (sem dois-pontos) → conjunto, que descarta repetições e não tem ordem.",
    error="`[]` cria lista (ordenada, com repetições); `{}` cria conjunto (itens únicos, sem ordem).",
)

st.divider()

stb.single_choice(
    "Onde fica o filtro numa compreensão, e o que ele faz?",
    [
        "Um `if` no fim — deixa passar só os itens em que a condição é verdadeira.",
        "Um `if` no começo — decide o tipo da coleção.",
        "Um `else` no fim — repete o item duas vezes.",
        "Não dá para filtrar numa compreensão.",
    ],
    0,
    success="Exato! `[x for x in dados if cond]` mantém só os itens que satisfazem `cond`.",
    error="O filtro é um `if` no fim: `[x for x in dados if cond]` seleciona quais itens entram.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações estão corretas?",
    {
        "`[expr for x in dados]` constrói uma lista nova a partir de `dados`.": True,
        "`{c: v for ...}` (com dois-pontos) constrói um dicionário.": True,
        "Um conjunto criado por compreensão remove valores repetidos.": True,
        "Uma compreensão pode ter um filtro `if` no fim.": True,
        "Toda compreensão precisa de um `if`.": False,
    },
    success="Mandou bem! Compreensão constrói coleções; `{c: v ...}` é dicionário; conjunto remove repetições; o `if` é opcional.",
    error="Revise: o `if` é opcional; `{c: v ...}` é dicionário; conjunto remove repetições.",
)

rodape_fases(__file__)
