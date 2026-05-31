"""
Autograder leve para as tarefas de código do curso Programação A.

Ideia: o aluno escreve código numa caixa de texto; este módulo executa o
código num namespace isolado e verifica o resultado contra casos de teste.

ATENÇÃO DE SEGURANÇA
--------------------
`exec` roda código arbitrário. Para uso em sala/local (ou alunos confiáveis)
está ok. Se você for publicar o app na nuvem com acesso aberto, troque por
uma sandbox de verdade (judge0, pyodide, subprocess com limites, etc.).
Aqui bloqueamos alguns builtins óbvios, mas isso NÃO é uma sandbox segura.
"""

import io
import contextlib
import traceback

# builtins liberados (suficientes para um curso introdutório)
_SAFE_BUILTINS = {
    "abs", "all", "any", "bool", "dict", "divmod", "enumerate", "filter",
    "float", "format", "frozenset", "int", "isinstance", "issubclass", "len",
    "list", "map", "max", "min", "next", "ord", "chr", "pow", "print", "range",
    "repr", "reversed", "round", "set", "slice", "sorted", "str", "sum",
    "tuple", "type", "zip", "True", "False", "None", "Exception", "ValueError",
    "TypeError", "ZeroDivisionError", "IndexError", "KeyError",
    # Orientação a objetos (Temas 9 e 10): `__build_class__` é o que o CPython
    # invoca ao executar um `class ...`; sem ele, definir classe dá
    # "NameError: __build_class__ not found". Os demais liberam OO idiomático.
    "__build_class__", "object", "super", "property", "staticmethod",
    "classmethod", "hasattr", "getattr", "setattr",
}


def _build_namespace():
    import builtins
    safe = {name: getattr(builtins, name) for name in _SAFE_BUILTINS
            if hasattr(builtins, name)}
    # `__name__` precisa existir nos globals: o corpo de toda classe roda
    # `__module__ = __name__`. Sem isso, dá "NameError: name '__name__' ...".
    return {"__builtins__": safe, "__name__": "__main__"}


def run_code(student_code, stdin_text=""):
    """Executa o código e devolve (ok, saida_stdout, erro_ou_None)."""
    ns = _build_namespace()
    stdout = io.StringIO()
    try:
        if stdin_text:
            import sys
            sys.stdin = io.StringIO(stdin_text)
        with contextlib.redirect_stdout(stdout):
            exec(student_code, ns)
        return True, stdout.getvalue(), None, ns
    except Exception:
        return False, stdout.getvalue(), traceback.format_exc(limit=3), ns


def check_function(student_code, func_name, cases):
    """
    Verifica uma FUNÇÃO definida pelo aluno.

    cases: lista de tuplas (args, esperado), onde args é uma tupla.
        ex: [((2, 3), 5), ((0, 0), 0)]

    Devolve (passou_tudo, lista_de_resultados).
    Cada resultado: dict(args, esperado, obtido, ok, erro).
    """
    ok_exec, _saida, erro, ns = run_code(student_code)
    if not ok_exec:
        return False, [{"args": "—", "esperado": "—", "obtido": "—",
                        "ok": False, "erro": erro}]
    func = ns.get(func_name)
    if not callable(func):
        return False, [{"args": "—", "esperado": "—", "obtido": "—",
                        "ok": False,
                        "erro": f"Não encontrei a função `{func_name}`."}]
    resultados = []
    todos_ok = True
    for args, esperado in cases:
        try:
            obtido = func(*args)
            ok = obtido == esperado
        except Exception:
            obtido = "ERRO"
            ok = False
        todos_ok = todos_ok and ok
        resultados.append({"args": args, "esperado": esperado,
                           "obtido": obtido, "ok": ok, "erro": None})
    return todos_ok, resultados


def check_output(student_code, esperado, stdin_text=""):
    """Verifica a SAÍDA (stdout) de um programa, ignorando espaços nas pontas."""
    ok_exec, saida, erro, _ns = run_code(student_code, stdin_text)
    if not ok_exec:
        return False, saida, erro
    return saida.strip() == esperado.strip(), saida, None
