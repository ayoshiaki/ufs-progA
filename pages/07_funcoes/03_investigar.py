import streamlit as st
import streamlit_book as stb

st.subheader("Fase 3 — 🔍 Investigar")
st.markdown("Agora o *porquê*. Pense na diferença entre `print` e `return`.")

stb.single_choice(
    "Por que usar `return` em vez de `print` quando a função calcula um valor?",
    [
        "São a mesma coisa; tanto faz.",
        "Porque `return` entrega o valor para quem chamou — dá para reaproveitar em outra conta.",
        "Porque `print` não funciona dentro de funções.",
        "Porque `return` é mais rápido de digitar.",
    ],
    1,
    success="Isso! `print` só mostra na tela; `return` devolve o valor, que você pode somar, guardar ou passar adiante.",
    error="A diferença-chave: `return` ENTREGA o valor (reutilizável); `print` só o mostra na tela.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre funções estão corretas?",
    {
        "Uma função pode ter vários parâmetros, separados por vírgula.": True,
        "Uma função sem `return` devolve `None`.": True,
        "A mesma função pode ser chamada várias vezes com valores diferentes.": True,
        "O código dentro do `def` roda na hora em que é definido.": False,
    },
    success="Mandou bem! Vários parâmetros, `None` sem `return`, reuso à vontade — e o corpo só roda quando a função é CHAMADA.",
    error="Revise: quando o corpo de uma função executa — ao definir ou ao chamar? E o que ela devolve sem `return`?",
)
