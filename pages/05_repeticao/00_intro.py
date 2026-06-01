import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** dada uma lista de notas, calcular a **média** da turma.

Você *poderia* somar nota por nota na mão... mas e se a turma tiver 300 alunos?
A ideia central aqui é a **repetição**: dar a mesma instrução muitas vezes sem
reescrevê-la. Em Python, o laço `for` percorre cada item de uma coleção.

> 💭 **Pense antes de avançar:** para tirar a média você precisa de duas coisas
> que vão *mudando* a cada volta do laço. Quais são?
"""
)

st.markdown(
    """
**E quando você não sabe quantas voltas serão?** O `for` é ótimo para percorrer
algo *conhecido* (uma lista, ou `range(n)`). Mas e "repita **até** o usuário
acertar a senha"? Não dá para saber de antemão quantas tentativas. Para isso
existe o `while`: ele repete **enquanto** uma condição for verdadeira.

Todo `while` tem **três peças**:

```python
contador = 3                 # 1) INICIALIZAR antes do laço
while contador > 0:          # 2) CONDIÇÃO testada a cada volta
    print(contador)
    contador = contador - 1  # 3) ATUALIZAR — aproxima a condição de ficar falsa
print("Fim!")
```

⚠️ **Laço infinito:** se você esquecer de **atualizar** (o passo 3), a condição
nunca fica falsa e o programa trava, repetindo para sempre.

**`for` ou `while`?**

- **`for`** — quando você sabe **o que percorrer** (os itens de uma lista) ou
  **quantas vezes** repetir (`range(n)`).
- **`while`** — quando você repete **até uma condição mudar** e não sabe quantas
  voltas serão (até acertar, até o saldo zerar, até a resposta convergir).

> 💭 **Pense antes de avançar:** quantas vezes o laço acima imprime algo? E o
> que aconteceria se a linha `contador = contador - 1` fosse esquecida?
"""
)

st.caption(
    "📖 **Documentação oficial do Python:** [Controle de fluxo — `for`, `range` e `while`](https://docs.python.org/pt-br/3/tutorial/controlflow.html)."
)

rodape_fases(__file__)
