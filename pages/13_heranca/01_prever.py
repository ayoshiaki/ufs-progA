import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''class Forma:
    def area(self):
        return 0

class Retangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

r = Retangulo(3, 4)
print(r.area())''',
    language="python",
)

stb.true_or_false(
    "Este programa imprime `12`.",
    True,
    success="Isso! `Retangulo` sobrescreve `area()` com `base * altura` = 3 × 4 = 12.",
    error="`Retangulo.area()` devolve `base * altura` = 3 × 4 = 12.",
)

st.divider()

st.code(
    '''formas = [Retangulo(2, 5), Retangulo(3, 3)]
total = 0
for f in formas:
    total = total + f.area()
print(total)''',
    language="python",
)

stb.single_choice(
    "Quanto o programa imprime?",
    [
        "19",
        "10",
        "9",
        "25",
    ],
    0,
    success="Exato! As áreas são 2×5=10 e 3×3=9; somadas dão 19. O `for` chama `.area()` em cada forma sem precisar saber o tipo.",
    error="Some as áreas: 2×5=10 e 3×3=9 → 19.",
)

rodape_fases(__file__)
