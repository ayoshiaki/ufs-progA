import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''try:
    nota = float("abc")
    print("virou número:", nota)
except ValueError:
    print("não dá para converter")''',
    language="python",
)

stb.true_or_false(
    'Este programa imprime `não dá para converter`.',
    True,
    success="Isso! `float(\"abc\")` lança `ValueError`. O `try` captura o erro e desvia para o `except`.",
    error="`float(\"abc\")` dá erro (ValueError). O `try/except` captura isso e roda o bloco do `except`.",
)

st.divider()

st.code(
    '''valores = ["7", "x", "9"]
soma = 0
for v in valores:
    try:
        soma = soma + float(v)
    except ValueError:
        pass
print(soma)''',
    language="python",
)

stb.single_choice(
    "Quanto vale `soma` no fim?",
    [
        "16.0",
        "7.0",
        "9.0",
        "O programa dá erro no \"x\".",
    ],
    0,
    success='Exato! O `"x"` é pulado pelo `except`; sobram 7 e 9, somando 16.0.',
    error='O `except` ignora o `"x"`. Sobram 7 + 9 = 16.0 — sem o programa quebrar.',
)
