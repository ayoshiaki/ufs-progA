"""
Testes do autograder server-side (utils/autograder.py).

Sem framework — rode direto:
    python tests/test_autograder.py

Cobre o bug do `__build_class__` (definição de classe sob builtins restritos),
que quebrava as fases Rodar/Modificar dos Temas 9 e 10.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils.autograder import check_output, check_function


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


def test_classe_simples():
    codigo = ("class ContaBancaria:\n"
              "    def __init__(self, saldo):\n"
              "        self.saldo = saldo\n"
              "    def depositar(self, valor):\n"
              "        self.saldo = self.saldo + valor\n"
              "c = ContaBancaria(100)\n"
              "c.depositar(50)\n"
              "print(c.saldo)")
    ok, saida, erro = check_output(codigo, "150")
    _ok("classe define e roda (era NameError __build_class__)", ok and erro is None)


def test_heranca_e_polimorfismo():
    codigo = ("class Forma:\n"
              "    def area(self):\n"
              "        return 0\n"
              "class Retangulo(Forma):\n"
              "    def __init__(self, b, h):\n"
              "        self.b = b; self.h = h\n"
              "    def area(self):\n"
              "        return self.b * self.h\n"
              "print(Retangulo(3, 4).area())")
    ok, _saida, _erro = check_output(codigo, "12")
    _ok("herança + sobrescrita de método", ok)


def test_super():
    codigo = ("class A:\n"
              "    def __init__(self):\n"
              "        self.x = 1\n"
              "class B(A):\n"
              "    def __init__(self):\n"
              "        super().__init__()\n"
              "        self.y = 2\n"
              "b = B()\n"
              "print(b.x + b.y)")
    ok, _s, _e = check_output(codigo, "3")
    _ok("super() funciona", ok)


def test_classe_via_check_function():
    # check_function também roda código que define classe + uma função usuária
    codigo = ("class Conta:\n"
              "    def __init__(self, s): self.s = s\n"
              "def saldo_apos_saque(inicial, valor):\n"
              "    c = Conta(inicial)\n"
              "    if valor <= c.s: c.s -= valor\n"
              "    return c.s")
    ok, _res = check_function(codigo, "saldo_apos_saque", [((100, 30), 70), ((50, 80), 50)])
    _ok("check_function com classe interna", ok)


def test_regressao_nao_oo():
    ok1, _s, _e = check_output('print("Total:", 5 * 3)', "Total: 15")
    ok2, _s, _e = check_output(
        's=0\nfor v in ["7","x","9"]:\n try: s+=float(v)\n except ValueError: pass\nprint(s)',
        "16.0")
    _ok("código não-OO continua funcionando (regressão)", ok1 and ok2)


def test_negativo_classe_errada_nao_passa():
    # depositar quebrado: NÃO pode passar por engano
    codigo = ("class C:\n"
              "    def __init__(self, x): self.saldo = x\n"
              "    def depositar(self, v): pass\n"
              "c = C(100); c.depositar(50); print(c.saldo)")
    ok, _s, _e = check_output(codigo, "150")
    _ok("classe errada corretamente NÃO passa", not ok)


if __name__ == "__main__":
    funcs = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for f in funcs:
        f()
    print(f"\n{len(funcs)} testes passaram.")
