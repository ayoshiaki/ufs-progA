"""
Bússola de navegação do livro Programação A.

Fonte única de verdade para tema/fase. Cada página chama uma função passando
`__file__`; o tema e a fase são DERIVADOS do caminho (pasta = tema, prefixo do
arquivo = fase), então não há número para repassar à mão em 60 arquivos.

    from utils.navegacao import cabecalho
    cabecalho(__file__)

Usa apenas primitivas nativas do Streamlit (sem HTML cru), incluindo a sintaxe
de cor do markdown (`:gray[...]`).
"""

from pathlib import Path

import streamlit as st

# Espelha as opções de streamlit_app.py, sem o prefixo numérico.
# Se mudar lá, mude aqui também.
TEMAS = {
    1: "Pensamento computacional",
    2: "Tipos e expressões",
    3: "Expressões booleanas",
    4: "Condicionais",
    5: "Repetição",
    6: "Listas, tuplas e dicionários",
    7: "Compreensões",
    8: "Strings",
    9: "Funções",
    10: "Recursão",
    11: "Funções de ordem superior",
    12: "Fluxo de dados: map, filter, reduce",
    13: "Arquivos e erros",
    14: "Introdução a objetos",
    15: "OO: herança e polimorfismo",
}

# Fase -> (emoji, nome). Espelha o método PRIMM da página de boas-vindas.
FASES = {
    1: ("🔮", "Prever"),
    2: ("▶️", "Rodar"),
    3: ("🔍", "Investigar"),
    4: ("🔧", "Modificar"),
    5: ("🛠️", "Criar"),
}

TOTAL_TEMAS = len(TEMAS)


def _tema(arquivo):
    """Número do tema a partir do nome da pasta (ex.: '02_tipos' -> 2)."""
    return int(Path(arquivo).parent.name.split("_")[0])


def _fase(arquivo):
    """Número da fase a partir do nome do arquivo (ex.: '03_investigar' -> 3)."""
    return int(Path(arquivo).stem.split("_")[0])


def cabecalho(arquivo):
    """Cabeçalho-bússola das fases 1–5: breadcrumb do tema + trilha PRIMM."""
    t, f = _tema(arquivo), _fase(arquivo)
    st.caption(f"Tema {t} · {TEMAS[t]}")
    colunas = st.columns(len(FASES))
    for coluna, num in zip(colunas, FASES):
        emoji, nome = FASES[num]
        if num == f:
            coluna.markdown(f"{emoji} **{nome}**")
        else:
            coluna.markdown(f"{emoji} :gray[{nome}]")
    st.caption(f"Fase {f} de {len(FASES)}")
    st.divider()


def cabecalho_intro(arquivo):
    """Cabeçalho da fase 0 (Aquecimento): situa o tema no curso inteiro."""
    t = _tema(arquivo)
    st.caption(f"Tema {t} de {TOTAL_TEMAS}")
    st.title(f"Tema {t} · {TEMAS[t]}")
    st.subheader("Fase 0 — Aquecimento")


def _rotulo_fase(num):
    """Rótulo curto de uma fase para os botões de navegação."""
    if num == 0:
        return "Aquecimento"
    emoji, nome = FASES[num]
    return f"{emoji} {nome}"


def rodape_fases(arquivo):
    """Botões de navegação entre fases no rodapé de cada página.

    Reaproveita o mesmo mecanismo dos botões ‹ › do topo (streamlit_book muda
    `st.session_state.page_number`), então as duas navegações ficam em sincronia.
    """
    from streamlit_book.file_reader import on_previous_click, on_next_click

    t, f = _tema(arquivo), _fase(arquivo)
    st.divider()
    esquerda, direita = st.columns(2)
    if f > 0:
        esquerda.button(
            f"‹ {_rotulo_fase(f - 1)}", key=f"nav_prev_{t}_{f}",
            on_click=on_previous_click, use_container_width=True,
        )
    if f < len(FASES):
        direita.button(
            f"{_rotulo_fase(f + 1)} ›", key=f"nav_next_{t}_{f}",
            on_click=on_next_click, use_container_width=True,
        )


def rodape_tema(arquivo):
    """Fechamento da fase 5 (Criar): celebra e aponta o próximo passo real.

    Vem logo após `rodape_fases`, que já desenha o divisor; por isso não desenha
    outro aqui.
    """
    t = _tema(arquivo)
    if t < TOTAL_TEMAS:
        st.success(
            f"✅ **Tema {t} de {TOTAL_TEMAS} concluído!** Depois de baixar o "
            f"comprovante, abra o **menu lateral** e siga para o "
            f"**Tema {t + 1} · {TEMAS[t + 1]}**."
        )
    else:
        st.success(
            f"🎉 **Você completou os {TOTAL_TEMAS} temas de Programação A!** "
            "Do pensamento computacional à orientação a objetos — parabéns."
        )


def legenda_fases():
    """Fila das 5 fases PRIMM, para a página de boas-vindas."""
    colunas = st.columns(len(FASES))
    for coluna, num in zip(colunas, FASES):
        emoji, nome = FASES[num]
        coluna.markdown(f"### {emoji}")
        coluna.caption(nome)


def mapa_curso():
    """Grade com todos os temas (faixas de 5), para a página de boas-vindas."""
    numeros = list(TEMAS)
    for inicio in range(0, len(numeros), 5):
        faixa = numeros[inicio:inicio + 5]
        colunas = st.columns(len(faixa))
        for coluna, t in zip(colunas, faixa):
            coluna.markdown(f"**{t}**")
            coluna.caption(TEMAS[t])
