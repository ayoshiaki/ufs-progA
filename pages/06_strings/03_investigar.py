import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê*. Pense em como comparar textos com segurança.")

stb.single_choice(
    'Por que `"Arara" == "arara"` é `False` em Python?',
    [
        "Porque uma tem mais letras que a outra.",
        "Porque o `A` maiúsculo e o `a` minúsculo são caracteres diferentes.",
        "Porque o Python não compara textos.",
        "Não é False; é True.",
    ],
    1,
    success="Isso! Para o computador, `A` e `a` têm códigos diferentes. Por isso, antes de comparar, costumamos usar `.lower()` nos dois lados.",
    error="Maiúscula e minúscula são caracteres distintos. Para ignorar a diferença, aplique `.lower()` antes de comparar.",
)

st.divider()

stb.multiple_choice(
    "Quais afirmações sobre strings estão corretas?",
    {
        "`texto[::-1]` devolve o texto invertido.": True,
        "`.lower()` ajuda a comparar ignorando maiúsculas/minúsculas.": True,
        '`"a e a".replace(" ", "")` remove os espaços, virando `"aea"`.': True,
        'Numa f-string, `f"{2 + 3}"` vira `"5"` (a expressão é calculada).': True,
        "Strings podem ter um caractere trocado com `texto[0] = \"X\"`.": False,
    },
    success="Mandou bem! Fatiar, `.lower()`, `.replace()` e f-strings criam textos novos — e você NÃO pode alterar uma letra no lugar (string é imutável).",
    error="Revise: dá para fazer `texto[0] = \"X\"`? (Não — string é imutável.) E o que aparece dentro de `{ }` numa f-string é avaliado.",
)

rodape_fases(__file__)
