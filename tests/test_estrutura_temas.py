"""
Teste estrutural dos temas PRIMM — sem framework, sem dependências externas.

Garante que as duas fontes-espelho (streamlit_app.py e utils/navegacao.py) e as
pastas de páginas concordam sobre quantos/quais temas existem. Lê os arquivos
via `ast`, então NÃO importa streamlit (que pode não estar instalado).

Rode direto:
    python tests/test_estrutura_temas.py
"""

import ast
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
PAGES = RAIZ / "pages"
FASES = ["00_intro", "01_prever", "02_rodar", "03_investigar",
         "04_modificar", "05_criar"]


def _pastas_de_tema():
    return [p for p in PAGES.iterdir() if p.is_dir() and p.name[:2].isdigit()]


def _temas_no_disco():
    return sorted(int(p.name.split("_")[0]) for p in _pastas_de_tema())


def _nomes_em_navegacao():
    arvore = ast.parse((RAIZ / "utils" / "navegacao.py").read_text())
    for node in ast.walk(arvore):
        if (isinstance(node, ast.Assign)
                and any(isinstance(t, ast.Name) and t.id == "TEMAS"
                        for t in node.targets)):
            return {k.value: v.value
                    for k, v in zip(node.value.keys, node.value.values)}
    raise AssertionError("TEMAS não encontrado em navegacao.py")


def _temas_em_navegacao():
    return sorted(_nomes_em_navegacao())


def _tamanhos_streamlit_app():
    arvore = ast.parse((RAIZ / "streamlit_app.py").read_text())
    for node in ast.walk(arvore):
        if (isinstance(node, ast.Call)
                and getattr(node.func, "attr", None) == "set_book_config"):
            kw = {k.arg: k.value for k in node.keywords}
            return {nome: len(kw[nome].elts)
                    for nome in ("options", "paths", "icons")}
    raise AssertionError("set_book_config não encontrado em streamlit_app.py")


def _ok(nome, cond):
    print(("✅" if cond else "❌"), nome)
    assert cond, nome


def test_toda_pasta_de_tema_tem_as_6_fases():
    for p in _pastas_de_tema():
        for fase in FASES:
            _ok(f"{p.name}/{fase}.py existe", (p / f"{fase}.py").exists())


def test_fontes_espelho_concordam():
    temas = _temas_no_disco()
    _ok("TEMAS (navegacao) == pastas no disco", _temas_em_navegacao() == temas)
    tam = _tamanhos_streamlit_app()
    _ok("options == paths == icons",
        tam["options"] == tam["paths"] == tam["icons"])
    # +1 pela página de Boas-vindas, que não é um tema PRIMM.
    _ok("len(options) == nº de temas + boas-vindas",
        tam["options"] == len(temas) + 1)


def test_temas_contiguos_de_1_a_n():
    temas = _temas_no_disco()
    _ok("temas numerados 1..N sem buracos",
        temas == list(range(1, len(temas) + 1)))


def test_cadeia_de_funcoes():
    nomes = _nomes_em_navegacao()

    def num(rotulo):
        achados = [n for n, nome in nomes.items() if nome == rotulo]
        _ok(f"tema '{rotulo}' existe (1x)", len(achados) == 1)
        return achados[0]

    # Decisão didática: o "cluster de funções" vem em sequência —
    # Funções → Recursão → Funções de ordem superior.
    funcoes = num("Funções")
    recursao = num("Recursão")
    hof = num("Funções de ordem superior")
    _ok("Recursão vem imediatamente após Funções", recursao == funcoes + 1)
    _ok("HOF vem imediatamente após Recursão", hof == recursao + 1)
    _ok("pasta de Recursão existe", any(
        p.name.endswith("_recursao") for p in _pastas_de_tema()))
    _ok("pasta de HOF existe", any(
        p.name.endswith("_hof") for p in _pastas_de_tema()))


def test_temas_novos_no_lugar_certo():
    nomes = _nomes_em_navegacao()

    def num(rotulo):
        achados = [n for n, nome in nomes.items() if nome == rotulo]
        _ok(f"tema '{rotulo}' existe (1x)", len(achados) == 1)
        return achados[0]

    # Decisão didática: Compreensões logo após Coleções (não precisa de funções);
    # map/filter/reduce logo após Funções de ordem superior (precisam de lambda).
    colecoes = num("Listas, tuplas e dicionários")
    compreensoes = num("Compreensões")
    matrizes = num("Matrizes")
    hof = num("Funções de ordem superior")
    fluxo = num("Fluxo de dados: map, filter, reduce")
    objetos = num("Introdução a objetos")
    encapsulamento = num("Encapsulamento")
    _ok("Compreensões vem imediatamente após Coleções", compreensoes == colecoes + 1)
    _ok("Matrizes vem imediatamente após Compreensões", matrizes == compreensoes + 1)
    _ok("Fluxo de dados vem imediatamente após HOF", fluxo == hof + 1)
    _ok("Encapsulamento vem imediatamente após Introdução a objetos",
        encapsulamento == objetos + 1)
    _ok("pasta de Compreensões existe", any(
        p.name.endswith("_compreensoes") for p in _pastas_de_tema()))
    _ok("pasta de Matrizes existe", any(
        p.name.endswith("_matrizes") for p in _pastas_de_tema()))
    _ok("pasta de Fluxo de dados existe", any(
        p.name.endswith("_fluxo_dados") for p in _pastas_de_tema()))
    _ok("pasta de Encapsulamento existe", any(
        p.name.endswith("_encapsulamento") for p in _pastas_de_tema()))


if __name__ == "__main__":
    test_toda_pasta_de_tema_tem_as_6_fases()
    test_fontes_espelho_concordam()
    test_temas_contiguos_de_1_a_n()
    test_cadeia_de_funcoes()
    test_temas_novos_no_lugar_certo()
    print("\n🎉 estrutura dos temas OK")
