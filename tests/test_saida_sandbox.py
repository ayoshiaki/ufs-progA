"""
Testa o conteúdo das fases Rodar/Modificar (independente de rodarem no servidor
ou no Pyodide): extrai `modelo` e `esperado` de cada exercício por AST e roda o
modelo em CPython capturando o stdout.

- Rodar (02_rodar.py): o modelo é "só rodar" → seu stdout DEVE ser o esperado.
- Modificar (04_modificar.py): o modelo está quebrado de propósito → seu stdout
  NÃO deve ser o esperado (ou ele lança erro).

Reconhece tanto `exercicio_saida` (server-side, antes da migração) quanto
`exercicio_saida_sandbox` (Pyodide, depois). Rode direto:

    /usr/local/bin/python3.11 tests/test_saida_sandbox.py
"""

import ast
import io
import contextlib
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAGES = RAIZ / "pages"
NOMES = {"exercicio_saida", "exercicio_saida_sandbox"}


def _exercicios(arquivo):
    """Lista (modelo, esperado) de cada chamada de exercicio_saida[_sandbox]."""
    achados = []
    arvore = ast.parse(arquivo.read_text())
    for node in ast.walk(arvore):
        if isinstance(node, ast.Call) and getattr(node.func, "id", None) in NOMES:
            kw = {k.arg: k.value for k in node.keywords}
            if "modelo" in kw and "esperado" in kw:
                achados.append((ast.literal_eval(kw["modelo"]),
                                ast.literal_eval(kw["esperado"])))
    return achados


def _stdout(codigo):
    """Roda o código em CPython e devolve (saida_strip, erro_ou_None)."""
    ns = {}
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(codigo, ns)
        return buf.getvalue().strip(), None
    except Exception as e:  # modelo de Modificar pode lançar — é "quebrado"
        return buf.getvalue().strip(), repr(e)


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


def test_modelos_de_rodar_produzem_o_esperado():
    for f in sorted(PAGES.glob("*/02_rodar.py")):
        for i, (modelo, esperado) in enumerate(_exercicios(f)):
            saida, erro = _stdout(modelo)
            rotulo = f"{f.parent.name}/02_rodar[{i}]"
            if erro:
                print(f"    {rotulo} erro inesperado: {erro}")
            _ok(f"{rotulo}: modelo imprime o esperado",
                erro is None and saida == str(esperado).strip())


def test_modelos_de_modificar_estao_quebrados():
    for f in sorted(PAGES.glob("*/04_modificar.py")):
        for i, (modelo, esperado) in enumerate(_exercicios(f)):
            saida, erro = _stdout(modelo)
            rotulo = f"{f.parent.name}/04_modificar[{i}]"
            # "Quebrado" = lança erro OU imprime algo diferente do esperado.
            quebrado = (erro is not None) or (saida != str(esperado).strip())
            _ok(f"{rotulo}: modelo está quebrado de propósito", quebrado)


def _runner_contrato(codigo, esperado):
    """Réplica em CPython da lógica do RUNNER do Pyodide (exec + stdout + strip)."""
    ns = {}
    buf = io.StringIO()
    erro = None
    ok = False
    try:
        with contextlib.redirect_stdout(buf):
            exec(codigo, ns)
        ok = buf.getvalue().strip() == esperado.strip()
    except Exception as e:
        erro = repr(e)
    return ok, buf.getvalue(), erro


def test_contrato_do_runner():
    ok, saida, erro = _runner_contrato("print('Total:', 5 * 3)", "Total: 15")
    _ok("saída correta → ok=True, sem erro", ok and erro is None)
    _ok("captura o stdout", saida.strip() == "Total: 15")
    ok2, _s, _e = _runner_contrato("print(10)", "20")
    _ok("saída errada → ok=False", not ok2)
    ok3, _s, erro3 = _runner_contrato("1/0", "x")
    _ok("exceção → ok=False e erro preenchido", (not ok3) and erro3 is not None)


if __name__ == "__main__":
    test_modelos_de_rodar_produzem_o_esperado()
    test_modelos_de_modificar_estao_quebrados()
    test_contrato_do_runner()
    print("\n🎉 conteúdo de Rodar/Modificar OK")
