import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** ler as **notas** de uma turma que vieram de um arquivo e
calcular a média — mas o mundo real é bagunçado: pode haver uma linha em branco,
um `"falta"` no lugar de um número, ou o arquivo pode nem existir.

Para lidar com isso, duas ideias:

- **Arquivos** — abrir e ler com `with open("notas.txt") as f:`
- **Tratamento de erros** — `try/except` para não deixar o programa quebrar
  quando aparece um dado inválido

```python
try:
    nota = float(linha)
except ValueError:
    pass   # ignora linhas que não são número
```

> 💭 **Pense antes de avançar:** se uma única linha do arquivo tiver `"abc"`,
> faz sentido o programa inteiro parar com erro? Ou é melhor *pular* essa linha
> e seguir somando as válidas?
"""
)

st.warning(
    """
⚠️ **Este livro roda online, no seu navegador.** Os exemplos executam numa
*sandbox* (WebAssembly) que **não enxerga os arquivos do seu computador** — um
`open("notas.txt")` não encontraria nenhum arquivo de verdade aqui, e não dá para
rodar um script que leia arquivos do disco. Por isso, neste tema:

- a parte de **abrir** o arquivo aparece só para você **ler e entender** (veja
  abaixo) — ela roda **no seu computador**, não nesta página;
- os exercícios que executam aqui já recebem as **linhas lidas** (uma lista de
  textos), para você focar no **tratamento de erros**, que é o coração do tema.
"""
)

st.markdown(
    "Assim seria a leitura de um arquivo **no seu computador** "
    "(código para entender — não roda nesta sandbox):"
)
st.code(
    '''# Com um arquivo notas.txt ao lado do programa:
with open("notas.txt") as f:      # abre o arquivo (e fecha sozinho no fim)
    for linha in f:               # percorre linha a linha
        print(linha.strip())      # .strip() remove o "enter" do fim da linha''',
    language="python",
)

st.caption(
    "📖 **Documentação oficial do Python:** [Erros e exceções (`try`/`except`)](https://docs.python.org/pt-br/3/tutorial/errors.html) e [Leitura e escrita de arquivos](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
