import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''def aplicar(f, x):
    return f(x)

def quadrado(n):
    return n * n

print(aplicar(quadrado, 4))''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `16`.",
    True,
    success="Isso! `aplicar(quadrado, 4)` chama `quadrado(4)`, que devolve `16`.",
    error="`aplicar(f, x)` devolve `f(x)`. Aqui `f` é `quadrado`, então é `quadrado(4) = 16`.",
)

st.divider()

st.code(
    '''dobro = lambda n: n * 2
print(dobro(5))''',
    language="python",
)

stb.single_choice(
    "O que aparece na tela?",
    [
        "10",
        "lambda n: n * 2",
        "5",
        "Erro: lambda não pode ser guardada numa variável",
    ],
    0,
    success="Exato! `lambda n: n * 2` é uma função; guardada em `dobro`, `dobro(5)` devolve `10`.",
    error="A `lambda` é uma função comum, só que sem nome. `dobro` virou essa função, então `dobro(5) = 10`.",
)

st.divider()
st.markdown("Agora uma função que **devolve** outra função:")

st.code(
    '''def somador(n):
    def soma(x):
        return x + n
    return soma

mais3 = somador(3)
print(mais3(10))''',
    language="python",
)

stb.single_choice(
    "O que este programa imprime?",
    [
        "13",
        "3",
        "10",
        "Erro: não dá para definir uma função dentro de outra",
    ],
    0,
    success="Isso! `somador(3)` devolve uma função que soma 3; `mais3(10)` faz `10 + 3 = 13`.",
    error="`somador(3)` fabrica uma função que soma 3 ao que receber. Então `mais3(10) = 10 + 3 = 13`.",
)

st.divider()

stb.single_choice(
    "E `somador(3)` sozinho, antes de chamar `mais3(...)` — o que é?",
    [
        "Uma função, que ainda vai ser chamada com um valor.",
        "O número 3.",
        "O número 0.",
        "Nada — `return` dentro de função interna não funciona.",
    ],
    0,
    success="Exato! `somador(3)` devolve uma FUNÇÃO; a conta só acontece quando você a chama, como em `mais3(10)`.",
    error="`somador` devolve a função interna `soma`. Então `somador(3)` é uma função; o `+` só roda quando ela é chamada.",
)

rodape_fases(__file__)
