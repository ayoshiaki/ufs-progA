import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense no papel do caso base e do caso recursivo.")

stb.single_choice(
    "O que acontece se uma função recursiva **não** tiver caso base (ou nunca chegar nele)?",
    [
        "Ela devolve `0` por segurança.",
        "Ela chama a si mesma sem parar, até o Python interromper com `RecursionError`.",
        "O Python ignora a recursão e roda só uma vez.",
        "Nada — funciona igual.",
    ],
    1,
    success="Isso! Sem um caso base que pare a corrente, a função se chama infinitamente e estoura o limite de recursão.",
    error="Sem caso base, não há freio: a função se chama para sempre, até o `RecursionError`.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre recursão estão corretas?",
    {
        "Toda função recursiva precisa de um **caso base** que pare a recursão.": True,
        "O caso recursivo deve chamar a função com uma entrada **menor**, rumo ao caso base.": True,
        "`fatorial(0)` devolve `1` direto, sem se chamar de novo.": True,
        "Recursão e laço (`for`/`while`) nunca resolvem o mesmo problema.": False,
    },
    success="Mandou bem! Caso base para parar, caso recursivo encolhendo a entrada — e muitos problemas podem ser resolvidos tanto com recursão quanto com laço.",
    error="Revise: qual o papel do caso base? E o caso recursivo aproxima ou afasta do caso base?",
)

rodape_fases(__file__)
