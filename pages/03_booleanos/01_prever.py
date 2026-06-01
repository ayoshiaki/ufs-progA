import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''idade = 20
tem_ingresso = True
print(idade >= 18 and tem_ingresso)''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `True`.",
    True,
    success="Isso! `20 >= 18` é `True` e `tem_ingresso` é `True`; com `and`, as duas verdadeiras dão `True`.",
    error="`and` é `True` só quando os dois lados são `True`. Aqui `20 >= 18` é `True` e `tem_ingresso` é `True`.",
)

st.divider()

st.code(
    '''idade = 16
tem_ingresso = True
print(idade >= 18 and tem_ingresso)''',
    language="python",
)

stb.single_choice(
    "Agora a idade é 16. O que aparece na tela?",
    [
        "False",
        "True",
        "16",
        "Erro",
    ],
    0,
    success="Exato! `16 >= 18` é `False`. Como o `and` exige os DOIS lados verdadeiros, o resultado é `False` — mesmo com ingresso.",
    error="`16 >= 18` é `False`. Com `and`, basta um lado `False` para o todo ser `False`.",
)

st.divider()

st.code(
    '''nota = 5
print(nota >= 6 or nota == 5)''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "True",
        "False",
        "5",
        "Erro",
    ],
    0,
    success="Isso! `5 >= 6` é `False`, mas `5 == 5` é `True`. O `or` precisa de só um lado verdadeiro: `True`.",
    error="`or` é `True` se PELO MENOS um lado for `True`. `nota == 5` é `True`, então o resultado é `True`.",
)

st.divider()
st.markdown("Agora **truthy/falsy** — como Python lê valores que não são `bool`:")

st.code(
    '''print(bool(""))
print(bool("oi"))''',
    language="python",
)

stb.single_choice(
    "O que aparece (duas linhas)?",
    [
        "False e True",
        "True e False",
        "True e True",
        "Erro: bool só aceita comparações",
    ],
    0,
    success="Isso! `\"\"` (texto vazio) é falsy → `False`; `\"oi\"` é texto não vazio → `True`.",
    error="Texto vazio `\"\"` é falsy (`False`); qualquer texto não vazio é truthy (`True`).",
)

st.divider()

st.code('print(not 0)', language="python")

stb.single_choice(
    "E aqui?",
    [
        "True",
        "False",
        "0",
        "Erro",
    ],
    0,
    success="Exato! `0` é falsy (lido como falso); o `not` inverte → `True`.",
    error="`0` é falsy. O `not` lê o `0` como falso e inverte para `True`.",
)

st.divider()

st.code(
    '''nome = ""
print(nome or "Anônimo")''',
    language="python",
)

stb.single_choice(
    "Com `nome` vazio, o que imprime?",
    [
        "Anônimo",
        "(uma linha em branco)",
        "True",
        "nome",
    ],
    0,
    success="Isso! `nome` é `\"\"` (falsy), então o `or` entrega o segundo valor: `Anônimo`.",
    error="`or` devolve o primeiro valor truthy. Como `nome` é `\"\"` (falsy), vai o segundo: `Anônimo`.",
)

rodape_fases(__file__)
