import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** uma loja precisa de um programa que pergunte o preço de
um produto e a quantidade comprada, e mostre o total a pagar.

Parece simples — e é. Mas resolver isso bem exige três ideias centrais da
computação que vamos destrinchar nas próximas fases:

- **Entrada** — como o programa recebe dados de fora (`input`)
- **Processamento** — como ele calcula (variáveis e contas)
- **Saída** — como ele devolve o resultado (`print`)

Essas três ideias são a estrutura *deste* programa. Por trás delas está um jeito
geral de atacar **qualquer** problema — os **4 pilares do pensamento
computacional**:

1. **Decomposição** — quebrar um problema grande em partes menores e tratáveis.
   *Na loja:* "receber o preço", "receber a quantidade", "calcular" e "mostrar".
2. **Reconhecimento de padrões** — perceber semelhanças e repetições.
   *Na loja:* "preço × quantidade" é o mesmo cálculo para qualquer produto.
3. **Abstração** — focar no essencial e ignorar o que não importa agora.
   *Na loja:* a cor ou a marca do produto não entram na conta — só preço e
   quantidade.
4. **Algoritmos** — descrever a solução como uma sequência de passos precisos e
   sem ambiguidade. *Na loja:* pergunte o preço → pergunte a quantidade →
   multiplique → mostre o total.

O termo **pensamento computacional** foi popularizado por **Jeannette Wing**, que
o descreveu como uma habilidade fundamental para *todos* — não apenas para quem
programa —, tão básica quanto ler, escrever e fazer contas (Wing, 2006).

> 💭 **Pense antes de avançar:** se você tivesse que explicar esse cálculo para
> uma pessoa que segue ordens ao pé da letra, quais passos exatos daria, e em
> que ordem? Isso é *pensamento computacional*: quebrar o problema em passos
> precisos e sem ambiguidade (um **algoritmo**).
"""
)

st.caption(
    "**Referência:** WING, J. M. *Computational Thinking.* Communications of the "
    "ACM, v. 49, n. 3, p. 33–35, 2006. "
    "DOI: [10.1145/1118178.1118215](https://doi.org/10.1145/1118178.1118215)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
