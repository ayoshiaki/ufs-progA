import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.componentes import exercicio_saida

st.subheader("Fase 2 — ▶️ Rodar")
st.markdown("Confirme sua previsão: este programa deve imprimir `60`.")

exercicio_saida(
    chave="t4_rodar",
    enunciado="Rode o acumulador de soma.",
    esperado="60",
    modelo="soma = 0\nfor n in [10, 20, 30]:\n    soma = soma + n\nprint(soma)",
    dica="É só rodar. Observe como `soma` muda a cada volta.",
)

st.info(
    "🔑 Padrão do **acumulador**: criar uma variável *antes* do laço (aqui `soma = 0`) "
    "e atualizá-la *dentro* do laço. Você vai reusar isso a vida toda."
)
