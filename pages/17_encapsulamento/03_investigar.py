import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em proteger as **regras** do objeto.")

stb.single_choice(
    "Para que serve encapsular o saldo (deixá-lo interno e só acessível por métodos)?",
    [
        "Para garantir que o saldo só mude seguindo as regras — sem alguém estragar o estado por fora.",
        "Para o programa rodar mais rápido.",
        "Para economizar memória.",
        "Só por estética; não muda nada na prática.",
    ],
    0,
    success="Isso! Concentrando as mudanças nos métodos, as regras (saldo não negativo etc.) ficam sempre protegidas.",
    error="Encapsular protege as REGRAS do objeto: o estado só muda por caminhos controlados, não por acesso direto.",
)

st.divider()

stb.single_choice(
    "O que o `_` no começo de `_saldo` significa, por convenção?",
    [
        '"Atributo interno — não mexa nele direto por fora."',
        "Que o atributo é constante e nunca muda.",
        "Que o atributo é público e pode ser alterado livremente.",
        "Que o atributo é um número.",
    ],
    0,
    success="Exato! O underscore é um combinado entre quem programa: é detalhe interno, mexa só pelos métodos.",
    error="Por convenção, `_nome` sinaliza 'uso interno' — não faz parte da interface pública da classe.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre encapsulamento em Python estão corretas?",
    {
        "`@property` deixa `c.saldo` ser **lido** como atributo, sem permitir atribuição direta.": True,
        "As regras (validação) ficam dentro dos métodos, não espalhadas pelo programa.": True,
        "Encapsular permite mudar o *interno* da classe sem quebrar quem só usa os métodos.": True,
        "`_saldo` é uma convenção que sinaliza 'atributo interno'.": True,
        "Com encapsulamento, ninguém mais consegue ler o saldo de jeito nenhum.": False,
    },
    success="Mandou bem! Encapsular controla o ACESSO (leitura por property, mudança por métodos) — não impede ler, impede estragar.",
    error="Revise: encapsular não esconde a leitura (a property expõe `saldo`); ele controla COMO o dado muda.",
)

rodape_fases(__file__)
