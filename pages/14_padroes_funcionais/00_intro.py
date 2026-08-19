import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** você já sabe que **funções são valores** — dá para
guardá-las, passá-las como argumento e devolvê-las (Temas 12 e 13). Pois quem
programa de verdade não para por aí: combina essas funções em **padrões com
nome**, soluções repetidas tantas vezes que ganharam apelido. Saber o nome ajuda
a reconhecer o problema e escrever a solução limpa de primeira.

Esta aula apresenta **cinco padrões clássicos da programação funcional**.
"""
)

st.markdown(
    """
**1. Tabela de despacho (*dispatch table*)** — um `dict` que mapeia uma chave a
uma **função**, no lugar de um `if/elif` comprido:

```python
acoes = {
    "dobrar":   lambda x: x * 2,
    "negar":    lambda x: -x,
    "quadrado": lambda x: x * x,
}
print(acoes["dobrar"](5))   # 10  — escolhe a função pela chave e a chama
```
"""
)

st.markdown(
    """
**2. `partial` — fixar argumentos** — `functools.partial(f, a)` devolve uma
**nova função** com alguns argumentos já preenchidos. Não executa nada ainda:

```python
from functools import partial

def soma(a, b):
    return a + b

soma10 = partial(soma, 10)   # "soma" com o primeiro argumento fixo em 10
print(soma10(5))             # 15
```
"""
)

st.markdown(
    """
**3. Pipe / composição** — encadear funções: a **saída de uma** vira a **entrada
da próxima**, como uma esteira:

```python
def pipe(valor, *funcs):
    for f in funcs:
        valor = f(valor)     # passa adiante o resultado
    return valor

print(pipe(3, lambda x: x + 1, lambda x: x * 2))   # (3+1)*2 = 8
```
"""
)

st.markdown(
    """
**4. *Pattern matching* (`match`/`case`)** — desmonta um valor pelo seu
**formato**, em vez de uma pilha de `if`:

```python
def descrever(ponto):
    match ponto:
        case (0, 0):       return "origem"
        case (x, 0):       return f"no eixo X em {x}"
        case (0, y):       return f"no eixo Y em {y}"
        case (x, y):       return f"em ({x}, {y})"

print(descrever((0, 5)))   # no eixo Y em 5
```
"""
)

st.markdown(
    """
**5. *Trampoline*** — para recursão **muito profunda**, Python estoura a pilha
(`RecursionError`). O truque do trampoline é a função **devolver o próximo passo**
(uma função a chamar) em vez de chamar a si mesma; um laço simples vai
"quicando" nesses passos até chegar ao resultado — sem empilhar chamadas:

```python
def trampolim(f, *args):
    resultado = f(*args)
    while callable(resultado):     # enquanto vier "o próximo passo"...
        resultado = resultado()    # ...quica nele
    return resultado
```

> 💭 **Pense antes de avançar:** no `dict acoes` acima, o que muda se você trocar
> `acoes["dobrar"](5)` por `acoes["quadrado"](5)`? E `partial(soma, 10)` — ele já
> calcula algo, ou só guarda o `10` para depois?
"""
)

st.caption(
    "📖 **Documentação oficial do Python:** [`functools` — `partial` e `reduce`]"
    "(https://docs.python.org/pt-br/3/library/functools.html) e "
    "[a instrução `match`](https://docs.python.org/pt-br/3/tutorial/controlflow.html#match-statements)."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
