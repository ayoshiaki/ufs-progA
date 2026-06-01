import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
Somar não basta — queremos a **média** das notas válidas. Parta do código que
soma e faça ele também **contar** quantas notas valeram, dividindo no fim.

Para `["7", "x", "9"]` (duas notas válidas), o programa deve imprimir:

```
8.0
```
"""
)

exercicio_saida(
    chave="t10_modificar",
    enunciado="Calcule a média das notas válidas.",
    esperado="8.0",
    modelo=(
        'valores = ["7", "x", "9"]\n'
        "soma = 0\n"
        "quantidade = 0\n"
        "for v in valores:\n"
        "    try:\n"
        "        soma = soma + float(v)\n"
        "        # conte mais uma nota valida aqui\n"
        "    except ValueError:\n"
        "        pass\n"
        "print(soma / quantidade)"
    ),
    dica="Dentro do `try`, depois de somar, faça `quantidade = quantidade + 1`. Assim só conta quando a conversão deu certo.",
)

rodape_fases(__file__)
