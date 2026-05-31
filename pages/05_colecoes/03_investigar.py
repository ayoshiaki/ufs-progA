import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense nas diferenças entre as estruturas.")

stb.single_choice(
    "Por que um dicionário é melhor que uma lista para uma agenda de telefones?",
    [
        "Porque dicionário é sempre mais rápido em tudo.",
        "Porque você busca direto pelo nome (a chave), sem saber a posição.",
        "Porque lista não guarda texto.",
        "Não há diferença prática.",
    ],
    1,
    success="Isso! Numa lista você precisaria saber a posição do contato; no dicionário, basta o nome.",
    error="O ganho do dicionário é buscar pela CHAVE (o nome), em vez de decorar a posição na lista.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações estão corretas?",
    {
        "Em listas, a primeira posição é o índice `0`.": True,
        "`agenda.get(\"Zé\", \"não encontrado\")` evita erro se a chave não existe.": True,
        "Uma tupla não pode ter seus itens trocados depois de criada.": True,
        "Dicionário guarda valores sem nenhuma chave associada.": False,
    },
    success="Mandou bem! Listas indexam do 0, `.get()` dá um padrão seguro, tuplas são imutáveis e todo valor no dicionário tem uma chave.",
    error="Revise: o que `.get()` faz quando a chave não existe? E o que torna a tupla diferente da lista?",
)

rodape_fases(__file__)
