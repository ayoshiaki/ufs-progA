import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense no papel do `self` e dos atributos.")

stb.single_choice(
    "Para que serve o `self` dentro de um método?",
    [
        "É só um nome decorativo, poderia ser omitido.",
        "Representa o próprio objeto, dando acesso aos seus atributos (`self.saldo`).",
        "É o nome da classe.",
        "Guarda o resultado do método.",
    ],
    1,
    success="Isso! `self` é a referência ao objeto em que o método foi chamado. Por ele você lê e altera os atributos daquele objeto.",
    error="`self` é o próprio objeto. É através dele (`self.saldo`) que o método acessa os dados daquela instância.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre classes e objetos estão corretas?",
    {
        "`__init__` é chamado automaticamente ao criar o objeto.": True,
        "Cada objeto tem a sua própria cópia dos atributos.": True,
        "Métodos são funções que pertencem à classe.": True,
        "Todos os objetos de uma classe compartilham o mesmo `self.saldo`.": False,
    },
    success="Mandou bem! `__init__` prepara cada objeto, e cada instância guarda os seus próprios atributos — eles não são compartilhados.",
    error="Revise: dois objetos da mesma classe dividem os atributos ou cada um tem o seu? (Cada um tem o seu.)",
)
