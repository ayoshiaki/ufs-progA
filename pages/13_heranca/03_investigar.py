import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em herança e polimorfismo.")

stb.single_choice(
    "Por que o `for f in formas: total += f.area()` funciona sem um `if` para cada tipo?",
    [
        "Porque todas as formas têm a mesma área.",
        "Porque cada objeto sabe responder ao seu próprio `area()` — isso é polimorfismo.",
        "Porque o Python adivinha o tipo certo na hora.",
        "Porque retângulos e círculos são a mesma classe.",
    ],
    1,
    success="Isso! Cada forma traz a sua versão de `area()`. Você chama o mesmo método e cada objeto faz a conta certa — polimorfismo.",
    error="A chave é o polimorfismo: o mesmo `f.area()` executa a versão própria de cada forma, sem `if`.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre herança estão corretas?",
    {
        "`class Circulo(Forma):` faz `Circulo` herdar de `Forma`.": True,
        "A classe filha pode sobrescrever um método da classe mãe.": True,
        "Polimorfismo é chamar o mesmo método em objetos de tipos diferentes.": True,
        "Herdar de uma classe obriga a reescrever todos os métodos dela.": False,
    },
    success="Mandou bem! A filha herda tudo, pode redefinir o que quiser, e o mesmo método se comporta conforme o objeto — sem precisar reescrever o que não muda.",
    error="Revise: ao herdar, você é obrigado a reescrever todos os métodos? (Não — só os que quiser mudar.)",
)

rodape_fases(__file__)
