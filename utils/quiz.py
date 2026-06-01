"""
Fachada de quizzes que EMBARALHA as alternativas.

Por que isto existe
-------------------
O `streamlit_book` mostra as opções exatamente na ordem em que são escritas no
código. Como, ao escrever a pergunta, a alternativa correta costuma ser digitada
primeiro, ela acaba caindo sempre no mesmo lugar — o aluno aprende a "chutar a
de cima". Aqui embaralhamos as opções antes de entregá-las ao streamlit_book.

O embaralhamento é DETERMINÍSTICO: a semente vem do próprio enunciado. Isso é
essencial porque o Streamlit re-executa o script inteiro a cada clique; se a
ordem mudasse a cada rerun, o `st.radio`/`st.checkbox` perderia a seleção do
aluno e a verificação quebraria. Mesma pergunta → mesma ordem, sempre; perguntas
diferentes → ordens diferentes.

Uso nas páginas (troca só a linha de import — a API continua idêntica):

    from utils import quiz as stb      # no lugar de: import streamlit_book as stb
    stb.single_choice(...)            # agora embaralha
    stb.multiple_choice(...)          # agora embaralha
    stb.true_or_false(...)            # repassado sem mudança
"""

import hashlib
import random

import streamlit_book as _stb


def _rng(semente_texto):
    """RNG estável derivado do texto (independe da versão do Python/máquina)."""
    digest = hashlib.sha256(semente_texto.encode("utf-8")).hexdigest()
    return random.Random(int(digest, 16))


def single_choice(question, options, answer_index, **kwargs):
    """Igual a streamlit_book.single_choice, mas com as opções embaralhadas."""
    correta = options[answer_index]
    embaralhadas = list(options)
    _rng(question).shuffle(embaralhadas)
    return _stb.single_choice(
        question, embaralhadas, embaralhadas.index(correta), **kwargs
    )


def multiple_choice(question, options_dict, **kwargs):
    """Igual a streamlit_book.multiple_choice, mas com as opções embaralhadas.

    Cada par (alternativa → True/False) é embaralhado junto, então o gabarito
    continua correto mesmo com as opções fora da ordem original.
    """
    itens = list(options_dict.items())
    _rng(question).shuffle(itens)
    return _stb.multiple_choice(question, dict(itens), **kwargs)


# Repassa todo o resto da API do streamlit_book (true_or_false, to_do_list,
# set_book_config, ...) sem alteração, para que `from utils import quiz as stb`
# seja um substituto completo de `import streamlit_book as stb`.
for _nome in dir(_stb):
    if not _nome.startswith("_") and _nome not in globals():
        globals()[_nome] = getattr(_stb, _nome)
