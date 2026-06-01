import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
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

rodape_fases(__file__)
