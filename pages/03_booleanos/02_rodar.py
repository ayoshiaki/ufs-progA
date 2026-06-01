import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Agora confirme. Rode a regra da portaria para quem tem **20 anos e está com
ingresso**. A previsão da fase anterior estava certa?
"""
)

exercicio_saida(
    chave="t3_rodar",
    enunciado="Faça este programa imprimir `True`.",
    esperado="True",
    modelo=(
        "idade = 20\n"
        "tem_ingresso = True\n"
        "print(idade >= 18 and tem_ingresso)"
    ),
    dica="Ja esta pronto no modelo — e so rodar para confirmar sua previsao.",
)

st.divider()
st.markdown(
    """
💡 **O que observar:** a expressão `idade >= 18 and tem_ingresso` é avaliada e
vira um único `bool`. Guarde isto: nos próximos temas, é exatamente esse
`True`/`False` que o `if` e o `while` vão usar para decidir o que fazer.
"""
)

rodape_fases(__file__)
