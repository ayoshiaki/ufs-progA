import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''palavra = "arara"
print(palavra[::-1])''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `arara` (a palavra invertida é igual à original).",
    True,
    success="Isso! `[::-1]` percorre a string de trás para frente. Como *arara* é palíndromo, o resultado é idêntico.",
    error="`[::-1]` inverte a string. Inverter *arara* dá... *arara* de novo — é um palíndromo.",
)

st.divider()

st.code(
    '''nome = "Python"
print(nome.lower())
print(len(nome))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "python\\n6",
        "PYTHON\\n6",
        "python\\n5",
        "Python\\n6",
    ],
    0,
    success="Exato! `.lower()` deixa tudo minúsculo (`python`) e `len` conta 6 letras.",
    error="`.lower()` deixa minúsculo; `len(\"Python\")` conta as 6 letras.",
)

st.divider()

st.code(
    '''nome = "Ana"
print(f"Oi, {nome}! Voce tem {3 + 2} mensagens")''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "Oi, Ana! Voce tem 5 mensagens",
        "Oi, {nome}! Voce tem {3 + 2} mensagens",
        "Oi, Ana! Voce tem 3 + 2 mensagens",
        "Oi, nome! Voce tem 5 mensagens",
    ],
    0,
    success="Isso! Numa f-string, cada `{...}` é trocado pelo seu valor: `{nome}` vira `Ana` e `{3 + 2}` é calculado para `5`.",
    error="Numa f-string, o que está entre chaves é avaliado: `{nome}` → `Ana`, e `{3 + 2}` → `5`.",
)

rodape_fases(__file__)
