import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em tipos e na ordem das operações.")

stb.single_choice(
    "Na expressão `c * 9 / 5 + 32`, qual conta o Python faz PRIMEIRO?",
    [
        "A soma `+ 32`, porque está no fim.",
        "A multiplicação e a divisão (da esquerda para a direita), antes da soma.",
        "A divisão `/ 5`, sempre antes de tudo.",
        "Tanto faz; a ordem não muda o resultado.",
    ],
    1,
    success="Isso! `*` e `/` têm prioridade sobre `+`. Só depois de `c*9/5` é que o `+32` acontece.",
    error="Lembre da ordem das operações: multiplicação e divisão vêm antes da soma.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre tipos em Python estão corretas?",
    {
        "`9 / 5` resulta em `float` (1.8).": True,
        "`9 // 5` resulta em `int` (1).": True,
        '`"20"` (com aspas) é um texto, não um número.': True,
        "`int` e `float` são o mesmo tipo.": False,
    },
    success="Mandou bem! `/` dá float, `//` dá int, e aspas transformam qualquer coisa em texto (`str`).",
    error="Revise: o que muda entre `/` e `//`? E o que as aspas fazem com um valor?",
)

rodape_fases(__file__)
