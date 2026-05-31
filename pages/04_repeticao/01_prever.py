import streamlit as st
import streamlit_book as stb

st.subheader("Fase 1 — 🔮 Prever")

st.code(
    '''soma = 0
for n in [10, 20, 30]:
    soma = soma + n
print(soma)''',
    language="python",
)

stb.single_choice(
    "O que esse programa imprime?",
    ["10", "30", "60", "[10, 20, 30]"],
    2,
    success="Isso! A cada volta `soma` acumula: 0→10→30→60.",
    error="Acompanhe `soma` em cada volta do laço, começando do 0.",
)

st.divider()

st.code(
    '''for i in range(3):
    print(i)''',
    language="python",
)

stb.single_choice(
    "E aqui, o que aparece (uma por linha)?",
    ["1 2 3", "0 1 2", "0 1 2 3", "3"],
    1,
    success="Exato! `range(3)` gera 0, 1, 2 — começa no 0 e NÃO inclui o 3.",
    error="`range(n)` vai de 0 até n-1. Quantos números são, e quais?",
)
