"""
Testa o helper `exercicio_script_sandbox` e os 7 "Criar" pré-Funções.

Reproduz em CPython o modelo de execução do RUNNER da sandbox (injeta as
entradas como variáveis, roda o script do aluno, lê `_res`) e:

  1. valida que uma solução de referência passa nos CASOS REAIS de cada página
     (extraídos por `ast`, sem importar streamlit);
  2. confirma o rigor anti-chute: um `_res` fixo NÃO passa em todos os casos;
  3. confirma que o script roda uma vez por caso (entradas isoladas).

Rode direto:
    python tests/test_script_sandbox.py
"""

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAGES = RAIZ / "pages"


def _rodar_script(codigo_aluno, casos):
    """Espelha o RUNNER: para cada caso, injeta entradas, exec, lê `_res`."""
    saidas = []
    for entradas, esperado in casos:
        ns = dict(entradas)
        try:
            exec(codigo_aluno, ns)
            obtido = ns.get("_res")
            ok = obtido == esperado
        except Exception as e:  # mesma captura por-caso do RUNNER
            obtido = f"ERRO: {e}"
            ok = False
        saidas.append((ok, obtido, esperado))
    return saidas


def _casos_da_pagina(caminho):
    """Extrai o argumento `casos=[...]` da chamada exercicio_script_sandbox."""
    arvore = ast.parse((PAGES / caminho).read_text())
    for node in ast.walk(arvore):
        if (isinstance(node, ast.Call)
                and getattr(node.func, "id", None) == "exercicio_script_sandbox"):
            for kw in node.keywords:
                if kw.arg == "casos":
                    return ast.literal_eval(kw.value)
    raise AssertionError(f"exercicio_script_sandbox não encontrado em {caminho}")


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


# Solução de referência (sem `def`) para cada tema pré-Funções.
SOLUCOES = {
    "01_pensamento_computacional/05_criar.py": "_res = preco * quantidade",
    "02_tipos/05_criar.py": "_res = c * 9 / 5 + 32",
    "03_booleanos/05_criar.py": "_res = idade >= 18 and tem_ingresso",
    "04_condicionais/05_criar.py": (
        "if media >= 7:\n"
        "    _res = 'Aprovado'\n"
        "elif media >= 5:\n"
        "    _res = 'Recuperação'\n"
        "else:\n"
        "    _res = 'Reprovado'"
    ),
    "05_repeticao/05_criar.py": "_res = sum(notas) / len(notas) if notas else 0",
    "06_colecoes/05_criar.py": '_res = agenda.get(nome, "não encontrado")',
    "07_compreensoes/05_criar.py": "_res = [n * n for n in numeros if n % 2 == 0]",
    "08_matrizes/05_criar.py": "_res = [sum(linha) for linha in tabuleiro]",
    "09_strings/05_criar.py": (
        "t = texto.lower().replace(' ', '')\n"
        "_res = t == t[::-1]"
    ),
}


def test_solucoes_de_referencia_passam_nos_casos_reais():
    for pagina, solucao in SOLUCOES.items():
        casos = _casos_da_pagina(pagina)
        _ok(f"{pagina}: tem ao menos 3 casos", len(casos) >= 3)
        saidas = _rodar_script(solucao, casos)
        todos = all(ok for ok, _, _ in saidas)
        if not todos:
            for ok, obtido, esperado in saidas:
                if not ok:
                    print(f"    caso falhou: obtido={obtido!r} esperado={esperado!r}")
        _ok(f"{pagina}: solução de referência passa em todos os casos", todos)


def test_chute_fixo_nao_passa():
    # Um aluno que "chuta" _res fixo deve falhar — prova do rigor multi-caso.
    casos = _casos_da_pagina("01_pensamento_computacional/05_criar.py")
    primeiro_esperado = casos[0][1]
    chute = f"_res = {primeiro_esperado!r}"
    saidas = _rodar_script(chute, casos)
    passou_todos = all(ok for ok, _, _ in saidas)
    _ok("chute fixo (_res constante) NÃO passa em todos os casos", not passou_todos)


def test_entradas_isoladas_entre_casos():
    # Cada caso roda num namespace novo: lixo de um caso não vaza para o outro.
    codigo = "_res = sobra if 'sobra' in dir() else preco\nsobra = 999"
    casos = [({"preco": 1}, 1), ({"preco": 2}, 2)]
    saidas = _rodar_script(codigo, casos)
    _ok("namespace novo por caso (sem vazamento de estado)",
        all(ok for ok, _, _ in saidas))


if __name__ == "__main__":
    test_solucoes_de_referencia_passam_nos_casos_reais()
    test_chute_fixo_nao_passa()
    test_entradas_isoladas_entre_casos()
    print("\n🎉 script_sandbox + 7 Criar pré-Funções OK")
