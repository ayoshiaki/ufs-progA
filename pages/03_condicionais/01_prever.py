import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown("Leia o código **sem rodar** e responda. Depois confirmamos na próxima fase.")

st.code(
    '''media = 6
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")''',
    language="python",
)

stb.true_or_false(
    "Para `media = 6`, este programa imprime `Recuperação`.",
    True,
    success="Isso! `6 >= 7` é falso, então cai no `elif`: `6 >= 5` é verdadeiro → Recuperação.",
    error="Teste cada condição em ordem: `6 >= 7`? Não. `6 >= 5`? Sim → Recuperação.",
)

st.divider()

st.code(
    '''media = 9
if media >= 5:
    print("Recuperação")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")''',
    language="python",
)

stb.single_choice(
    "Com a ordem trocada acima, o que um aluno de média 9 recebe?",
    [
        "Aprovado",
        "Recuperação",
        "Reprovado",
        "Aprovado e Recuperação",
    ],
    1,
    success="Exato! O primeiro `if` (`9 >= 5`) já é verdadeiro, então ele entra no Recuperação e os outros nem são testados. Ordem importa!",
    error="O Python para no PRIMEIRO teste verdadeiro. `9 >= 5` já é verdadeiro — ele nem chega no `elif`.",
)
