import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense no papel de cada etapa da esteira.")

stb.single_choice(
    "Qual a diferença de papel entre `map` e `filter`?",
    [
        "`map` transforma cada item; `filter` decide quais itens ficam.",
        "`map` decide quais ficam; `filter` transforma cada item.",
        "Os dois fazem a mesma coisa, com nomes diferentes.",
        "`map` só funciona com números; `filter`, só com texto.",
    ],
    0,
    success="Isso! `map` muda cada item (mesma quantidade de saída); `filter` seleciona (pode sair menos).",
    error="`map` transforma cada item; `filter` mantém só os que passam no teste.",
)

st.divider()

stb.single_choice(
    "O que o `reduce` faz, diferente de `map` e `filter`?",
    [
        "Combina a coleção inteira num ÚNICO valor (soma, máximo, produto...).",
        "Devolve sempre uma lista do mesmo tamanho da entrada.",
        "Remove os itens repetidos da coleção.",
        "Ordena a coleção do menor para o maior.",
    ],
    0,
    success="Exato! `map`/`filter` devolvem uma coleção; `reduce` agrega tudo num só resultado.",
    error="`reduce` acumula os itens dois a dois até sobrar um único valor.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações estão corretas?",
    {
        "`reduce` precisa ser importado de `functools`.": True,
        "`map` e `filter` são preguiçosos; use `list(...)` para ver o resultado.": True,
        "A compreensão `[f(x) for x in dados if cond]` faz o papel de `map` + `filter`.": True,
        "`map`, `filter` e `reduce` recebem uma função como argumento.": True,
        "`map` sempre devolve menos itens do que recebeu.": False,
    },
    success="Mandou bem! `reduce` vem de functools; map/filter são preguiçosos; a compreensão cobre map+filter; todos recebem uma função.",
    error="Revise: `reduce` vem de functools; map/filter são preguiçosos; `map` devolve a MESMA quantidade de itens.",
)

rodape_fases(__file__)
