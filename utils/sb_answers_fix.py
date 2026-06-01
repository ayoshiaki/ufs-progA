"""
Conserto do `save_answer` do streamlit_book.

O original envolve cada campo em aspas mas NÃO escapa as aspas que aparecem
DENTRO do conteúdo (RFC-4180 exige duplicá-las). Como muitas perguntas/respostas
do curso contêm `"` — ex.: `print("Total:", total)` —, a aspa interna fecha o
campo cedo e a vírgula seguinte vira separador, corrompendo `tmp/answers.csv`.
Isso quebra a **Admin View** (`?user=admin`), que lê o arquivo com `pandas`.

Aqui gravamos via `csv.writer`, que escapa vírgulas e aspas corretamente, e
aplicamos o patch em TODOS os módulos do streamlit_book que já importaram
`save_answer` (cada `render_*` faz `from .answers import save_answer`, então
guarda a própria referência).

Uso (em streamlit_app.py, depois de `import streamlit_book`):

    from utils.sb_answers_fix import instalar
    instalar(st)
"""

import csv
import sys


def anexar_resposta(caminho, linha):
    """Acrescenta uma linha (lista de campos) em CSV válido (RFC-4180)."""
    with open(caminho, "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow(linha)


def instalar(st):
    """Substitui o save_answer do streamlit_book por uma versão que grava CSV válido."""
    import streamlit_book.answers as ans
    from streamlit_book.keywords import ANSWER_FILENAME

    def save_answer(question, is_correct, user_answer, correct_answer):
        ans.create_answer_file()
        anexar_resposta(ANSWER_FILENAME, [
            st.session_state.commit_hash,
            ans.get_datetime_string(),
            st.session_state.user_id,
            str(question).replace("\n", "\\n"),
            str(is_correct),
            str(user_answer).replace("\n", "\\n"),
            str(correct_answer).replace("\n", "\\n"),
        ])

    for mod in list(sys.modules.values()):
        nome = getattr(mod, "__name__", "")
        if nome.startswith("streamlit_book") and hasattr(mod, "save_answer"):
            mod.save_answer = save_answer
