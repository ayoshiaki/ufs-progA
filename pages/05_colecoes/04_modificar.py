import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown(
    """
A agenda cresceu. **Adicione** um novo contato — `"Caio"` com telefone
`"97773333"` — e depois imprima o telefone dele.

O programa deve imprimir:

```
97773333
```
"""
)

exercicio_saida(
    chave="t5_modificar",
    enunciado="Adicione o contato Caio e imprima o telefone dele.",
    esperado="97773333",
    modelo=(
        'agenda = {"Ana": "99991111", "Bia": "98882222"}\n'
        "# adicione o Caio aqui\n"
        'print(agenda["Caio"])'
    ),
    dica='Para inserir: `agenda["Caio"] = "97773333"` (antes do print).',
)

rodape_fases(__file__)
