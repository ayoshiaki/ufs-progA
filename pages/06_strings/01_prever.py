import streamlit as st
import streamlit_book as stb

st.subheader("Fase 1 — 🔮 Prever")
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
