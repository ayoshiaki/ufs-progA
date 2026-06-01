"""
Testa o conserto da gravação de respostas (utils/sb_answers_fix.anexar_resposta).

Garante que uma resposta com **aspas e vírgulas** (ex.: pergunta com
`print("Total:", total)` e resposta que é a repr de uma lista) é gravada em CSV
válido e relida corretamente pelo pandas — exatamente como a Admin View faz.

Rode direto:
    /usr/local/bin/python3.11 tests/test_answers_csv.py
"""

import csv
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from utils.sb_answers_fix import anexar_resposta

HEADER = ["commit_hash", "datetime", "user_id", "question",
          "correct?", "user_answer", "correct_answer"]


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


def test_round_trip_com_aspas_e_virgulas():
    linha = [
        "abc1234",
        "2026-06-01 10:00:00",
        "3",
        'Quais afirmações sobre `print("Total:", total)` estão corretas?',
        "False",
        "['`\"Total:\"` é literal, com vírgula', 'total é variável']",
        "['`\"Total:\"` é literal, com vírgula']",
    ]
    fd, caminho = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    try:
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(HEADER)
        anexar_resposta(caminho, linha)
        df = pd.read_csv(caminho)  # como a Admin View (answers_info) lê
        _ok("pandas lê 1 linha x 7 colunas", df.shape == (1, 7))
        _ok("pergunta (com aspas) preservada", df.iloc[0]["question"] == linha[3])
        _ok("user_answer (com aspas e vírgula) preservado",
            df.iloc[0]["user_answer"] == linha[5])
    finally:
        os.remove(caminho)


def test_varias_linhas_contam_certo():
    fd, caminho = tempfile.mkstemp(suffix=".csv")
    os.close(fd)
    try:
        with open(caminho, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(HEADER)
        for i in range(5):
            anexar_resposta(caminho, ["h", "t", str(i),
                                      'p, com "aspas"', "True", "a, b", "a, b"])
        df = pd.read_csv(caminho)
        _ok("5 linhas, 7 colunas, sem quebra", df.shape == (5, 7))
    finally:
        os.remove(caminho)


if __name__ == "__main__":
    test_round_trip_com_aspas_e_virgulas()
    test_varias_linhas_contam_certo()
    print("\n🎉 gravação de respostas em CSV válido OK")
