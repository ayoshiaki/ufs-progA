"""
Testa a fachada utils/quiz.py: as alternativas dos quizzes são embaralhadas,
o embaralhamento é estável entre reruns e o gabarito acompanha a opção correta.

Não sobe o Streamlit: substitui streamlit_book.single_choice/multiple_choice por
espiões que apenas registram os argumentos recebidos. Rode direto:

    python tests/test_quiz_embaralha.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import streamlit_book as stb_real
from utils import quiz


def _espiao():
    chamadas = []

    def fake(*args, **kwargs):
        chamadas.append((args, kwargs))
        return True, True

    return chamadas, fake


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


def test_single_choice_embaralha_mas_preserva_gabarito():
    chamadas, fake = _espiao()
    stb_real.single_choice = fake
    pergunta = "Qual a capital do Brasil?"
    opcoes = ["Brasília", "Rio de Janeiro", "São Paulo", "Salvador"]

    quiz.single_choice(pergunta, opcoes, 0, success="ok")
    (q, opts_vistas, idx), kw = chamadas[-1]

    _ok("pergunta repassada", q == pergunta)
    _ok("kwargs repassados", kw == {"success": "ok"})
    _ok("mesmas opções, só reordenadas", sorted(opts_vistas) == sorted(opcoes))
    _ok("ordem realmente mudou", opts_vistas != opcoes)
    _ok("índice aponta para a alternativa correta", opts_vistas[idx] == "Brasília")


def test_single_choice_estavel_entre_reruns():
    chamadas, fake = _espiao()
    stb_real.single_choice = fake
    pergunta = "2 + 2 = ?"
    opcoes = ["4", "3", "5", "22"]

    quiz.single_choice(pergunta, opcoes, 0)
    quiz.single_choice(pergunta, opcoes, 0)  # simula um segundo rerun
    primeira = chamadas[0][0][1]
    segunda = chamadas[1][0][1]
    _ok("ordem idêntica em reruns da mesma pergunta", primeira == segunda)


def test_perguntas_diferentes_ordens_diferentes():
    chamadas, fake = _espiao()
    stb_real.single_choice = fake
    opcoes = ["A", "B", "C", "D", "E", "F"]
    quiz.single_choice("Pergunta um", list(opcoes), 0)
    quiz.single_choice("Pergunta dois — outro enunciado", list(opcoes), 0)
    _ok("enunciados distintos geram ordens distintas",
        chamadas[0][0][1] != chamadas[1][0][1])


def test_multiple_choice_embaralha_e_mantem_pares():
    chamadas, fake = _espiao()
    stb_real.multiple_choice = fake
    pergunta = "Quais são linguagens de programação?"
    opcoes = {"Python": True, "HTTP": False, "Java": True, "JSON": False}

    quiz.multiple_choice(pergunta, opcoes, success="ok")
    (q, dic_visto), _kw = chamadas[-1]

    _ok("pergunta repassada", q == pergunta)
    _ok("mesmos pares, só reordenados", dic_visto == opcoes)
    _ok("ordem das chaves realmente mudou",
        list(dic_visto.keys()) != list(opcoes.keys()))
    _ok("gabarito acompanha cada alternativa",
        all(dic_visto[k] == opcoes[k] for k in opcoes))


def test_fachada_repassa_resto_da_api():
    _ok("true_or_false disponível na fachada", hasattr(quiz, "true_or_false"))
    _ok("to_do_list disponível na fachada", hasattr(quiz, "to_do_list"))
    _ok("set_book_config disponível na fachada", hasattr(quiz, "set_book_config"))


if __name__ == "__main__":
    test_single_choice_embaralha_mas_preserva_gabarito()
    test_single_choice_estavel_entre_reruns()
    test_perguntas_diferentes_ordens_diferentes()
    test_multiple_choice_embaralha_e_mantem_pares()
    test_fachada_repassa_resto_da_api()
    print("\n🎉 embaralhamento dos quizzes OK")
