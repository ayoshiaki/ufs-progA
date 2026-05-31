import streamlit as st
import streamlit_book as stb

st.subheader("Fase 3 — 🔍 Investigar")
st.markdown("Agora o *porquê*. Pense em como o Python percorre um `if/elif/else`.")

stb.single_choice(
    "Quando uma condição do `if` é verdadeira, o que acontece com os `elif` seguintes?",
    [
        "São todos testados também, por garantia.",
        "São ignorados — o Python sai do bloco assim que um teste dá verdadeiro.",
        "Só o último `elif` é testado.",
        "O programa dá erro.",
    ],
    1,
    success="Isso! Só um ramo executa: o do primeiro teste verdadeiro. Por isso a ordem do mais exigente para o menos exigente importa.",
    error="O `if/elif/else` escolhe UM ramo só: o primeiro verdadeiro. Os outros são pulados.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre condicionais estão corretas?",
    {
        "`media >= 7` devolve `True` ou `False`.": True,
        "Trocar a ordem dos testes pode mudar o resultado.": True,
        "O `else` não precisa de condição — é o caso que sobra.": True,
        "Todo `if` obrigatoriamente precisa de um `else`.": False,
    },
    success="Mandou bem! Comparações dão booleanos, a ordem importa, o `else` é opcional e cobre o resto.",
    error="Revise: o `else` é obrigatório? E o que uma comparação como `media >= 7` devolve?",
)
