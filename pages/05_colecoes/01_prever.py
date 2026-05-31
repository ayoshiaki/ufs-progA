import streamlit as st
import streamlit_book as stb

st.subheader("Fase 1 — 🔮 Prever")
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''agenda = {"Ana": "99991111", "Bia": "98882222"}
print(agenda["Ana"])''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `99991111`.",
    True,
    success='Isso! `agenda["Ana"]` busca o valor associado à chave `"Ana"`.',
    error='No dicionário, `agenda["Ana"]` devolve o VALOR ligado à chave `"Ana"` — o telefone dela.',
)

st.divider()

st.code(
    '''frutas = ["maçã", "banana", "uva"]
print(frutas[1])''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "maçã",
        "banana",
        "uva",
        "1",
    ],
    1,
    success="Exato! Em listas a contagem começa do ZERO: `frutas[0]` é maçã, `frutas[1]` é banana.",
    error="Cuidado: a posição começa em 0. `frutas[0]` = maçã, então `frutas[1]` = banana.",
)
