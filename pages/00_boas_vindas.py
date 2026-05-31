import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
import streamlit_book as stb
from utils.navegacao import mapa_curso, legenda_fases

st.title("🐍 Programação A")
st.caption("Do pensamento computacional à orientação a objetos — um problema de cada vez.")

st.markdown(
    """
Bem-vindo! Este curso é feito de **problemas com dificuldade crescente**.
São **10 temas**, e em cada um você não vai só assistir — vai **prever, rodar,
investigar, modificar e criar** código.

### Os 10 temas do curso
"""
)

mapa_curso()

st.markdown(
    """
Cada item do **menu lateral** é um desses 10 temas. Dentro dele, você avança
pelas mesmas **5 fases** com os botões **‹ ›** no topo.

### As 5 fases de cada tema (PRIMM)
"""
)

legenda_fases()

st.markdown(
    """
### O que você faz em cada fase
1. **🔮 Prever** — leia um trecho de código e adivinhe o que ele faz, *antes* de rodar.
2. **▶️ Rodar** — execute e confira se sua previsão estava certa.
3. **🔍 Investigar** — responda perguntas sobre *por que* o código se comporta assim.
4. **🔧 Modificar** — altere o código para mudar o comportamento.
5. **🛠️ Criar** — resolva um problema novo do zero. **Esta é a tarefa que você entrega.**

As fases 1–4 são curtas e de autocorreção (clique e veja na hora se acertou).
A fase 5 gera um **comprovante de entrega** para você anexar onde o professor indicar.

### Regras do jogo
- Tente prever **antes** de rodar — é aí que o aprendizado acontece.
- Errar é parte do processo: os testes existem para te dar pistas, não nota.
- Só avance de tema quando fechar a fase **Criar**.
"""
)

stb.to_do_list(
    {
        "Tenho Python 3.10+ instalado (ou vou usar o app na nuvem)": False,
        "Sei abrir e rodar este livro": False,
        "Entendi as 5 fases de cada tema": False,
        "Sei onde entregar o comprovante da fase Criar": False,
    },
    header="### ✅ Checklist antes de começar",
    success="Tudo pronto. Bora para o Tema 1!",
)
