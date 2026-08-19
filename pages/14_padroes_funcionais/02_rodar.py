import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.sandbox_pyodide import exercicio_saida_sandbox
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    "Rode o programa abaixo e confira suas previsões. Ele usa **três padrões "
    "juntos**: uma `partial`, uma **tabela de despacho** e um **pipe**."
)

exercicio_saida_sandbox(
    chave="t14_rodar",
    enunciado="Rode e confirme a saída:",
    esperado="22",
    modelo=(
        "from functools import partial\n"
        "\n"
        "def soma(a, b):\n"
        "    return a + b\n"
        "\n"
        "# partial: 'soma' com o primeiro argumento fixo em 10\n"
        "soma10 = partial(soma, 10)\n"
        "\n"
        "# tabela de despacho: nome -> função\n"
        "passos = {\n"
        "    \"mais10\": soma10,\n"
        "    \"dobrar\": lambda x: x * 2,\n"
        "}\n"
        "\n"
        "# pipe: aplica os passos em sequência\n"
        "def pipe(valor, *funcs):\n"
        "    for f in funcs:\n"
        "        valor = f(valor)\n"
        "    return valor\n"
        "\n"
        "print(pipe(1, passos[\"mais10\"], passos[\"dobrar\"]))"
    ),
    dica="Siga a esteira: começa em 1, `mais10` leva a 11, depois `dobrar` leva a 22.",
)

st.divider()
st.markdown(
    "💡 **O que observar:** `soma10` foi *fabricada* uma vez por `partial` e "
    "guardada na tabela como qualquer outra função. O `pipe` não sabe (nem "
    "precisa saber) o que cada passo faz — só repassa o resultado adiante."
)

rodape_fases(__file__)
