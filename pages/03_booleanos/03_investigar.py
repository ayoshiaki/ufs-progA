import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em como `and`, `or` e `not` combinam condições.")

stb.single_choice(
    "Quando `A and B` é `True`?",
    [
        "Quando pelo menos um dos dois é `True`.",
        "Somente quando A e B são, os dois, `True`.",
        "Quando A e B são diferentes.",
        "Sempre que A for `True`, não importa B.",
    ],
    1,
    success="Isso! O `and` exige os DOIS lados verdadeiros. Basta um `False` para o resultado ser `False`.",
    error="`and` só é `True` quando AMBOS os lados são `True`. (Quem aceita 'pelo menos um' é o `or`.)",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre expressões booleanas estão corretas?",
    {
        "`==` compara dois valores; `=` apenas atribui.": True,
        "`or` é `True` se pelo menos uma das condições for `True`.": True,
        "`not True` é `False` (o `not` inverte).": True,
        "Uma comparação como `idade >= 18` resulta em `True` ou `False`.": True,
        "`and` é `True` se pelo menos uma condição for `True`.": False,
    },
    success="Mandou bem! `==` compara, `or` aceita um lado, `not` inverte, e comparações viram `bool` — só o `and` exige os dois lados.",
    error="Revise: o que o `and` exige (um lado ou os dois)? E qual a diferença entre `=` e `==`?",
)

rodape_fases(__file__)
