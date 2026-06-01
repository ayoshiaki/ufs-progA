import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Mudança na regra: agora um **convidado VIP entra sem ingresso e sem idade
mínima**. Parta da expressão atual e use `or eh_vip` para liberar o VIP.

Para `idade = 16`, `tem_ingresso = False` e `eh_vip = True`, o programa deve
imprimir:

```
True
```
"""
)

exercicio_saida(
    chave="t3_modificar",
    enunciado="Acrescente `or eh_vip` para que o VIP possa entrar.",
    esperado="True",
    modelo=(
        "idade = 16\n"
        "tem_ingresso = False\n"
        "eh_vip = True\n"
        "# regra atual: 18+ E com ingresso\n"
        "print(idade >= 18 and tem_ingresso)"
    ),
    dica="Envolva a regra atual em parenteses e acrescente `or eh_vip`: "
         "`(idade >= 18 and tem_ingresso) or eh_vip`.",
)

rodape_fases(__file__)
