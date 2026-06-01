import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils.navegacao import cabecalho_intro, rodape_fases

cabecalho_intro(__file__)

st.markdown(
    """
**O problema do tema:** calcular o **fatorial** de um número. O fatorial de `5`
(escrito `5!`) é `5 × 4 × 3 × 2 × 1 = 120`.

Repare que esse problema se define **em termos de si mesmo**: `5!` é `5` vezes
`4!`; e `4!` é `4` vezes `3!`; e assim por diante. Quando um problema contém uma
versão menor dele mesmo, uma função pode **chamar a si mesma** para resolvê-lo —
isso é **recursão**.

Toda função recursiva precisa de duas partes:

- **Caso base** — a versão mais simples, que tem resposta direta e **para** a
  recursão. Para o fatorial: `0! = 1`.
- **Caso recursivo** — resolve o problema usando uma versão **menor** dele
  mesmo. Para o fatorial: `n! = n × (n - 1)!`.

```python
def fatorial(n):
    if n == 0:          # caso base
        return 1
    return n * fatorial(n - 1)   # caso recursivo
```

⚠️ **Sem caso base, a recursão nunca para** — a função fica chamando a si mesma
até o Python desistir com um erro (`RecursionError`). O caso base é o freio.

> 💭 **Pense antes de avançar:** já dava para fazer o fatorial com um laço `for`
> (Tema 5). Por que aprender recursão? Porque alguns problemas — como percorrer
> pastas dentro de pastas — são **naturalmente** recursivos, e a solução fica
> mais clara assim.
"""
)

st.markdown("**Quer ir além?** Abra os blocos abaixo para aprofundar.")

with st.expander("🧱 Recursão em estruturas (listas e dicionários)"):
    st.markdown(
        """
A recursão brilha quando os **dados** têm partes dentro de partes. Uma lista é
"o primeiro item **+** o resto" — e o resto é uma lista menor, rumo à lista
vazia (o caso base):

```python
def soma_lista(numeros):
    if numeros == []:                              # caso base: lista vazia
        return 0
    return numeros[0] + soma_lista(numeros[1:])    # primeiro + resto

soma_lista([10, 20, 30])   # 60
```

Quando a estrutura tem **níveis** — listas dentro de listas, como pastas dentro
de pastas — a recursão desce sozinha em cada nível:

```python
def soma_tudo(item):
    if isinstance(item, list):
        return sum(soma_tudo(parte) for parte in item)   # cada parte recursiva
    return item                                          # caso base: um número

soma_tudo([1, [2, 3], [4, [5, 6]]])   # 21
```

Vale igual para **dicionários** e **listas de dicionários** (ex.: um menu com
submenus, ou uma árvore de comentários): trate o caso simples direto e chame a
função nas partes compostas.
        """
    )

with st.expander("🪙 Recursão de cauda (tail recursion)"):
    st.markdown(
        """
Uma recursão é **de cauda** quando a chamada recursiva é a **última** coisa que a
função faz — não sobra nenhuma conta depois dela. Compare:

```python
# NÃO é de cauda: ainda falta "n * ..." depois que a chamada retorna
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# É de cauda: a chamada recursiva é a última operação; o resultado
# parcial viaja num parâmetro acumulador
def fatorial(n, acumulado=1):
    if n == 0:
        return acumulado
    return fatorial(n - 1, acumulado * n)
```

Em algumas linguagens, recursão de cauda é otimizada para não gastar pilha (vira
quase um laço). **Atenção: o Python NÃO faz essa otimização** — a versão de cauda
ainda tem o mesmo limite de profundidade. O valor do padrão, em Python, é a
**clareza** e a facilidade de **converter para um laço** quando preciso.
        """
    )

with st.expander("⚡ Memoização: não recalcular o que já foi calculado"):
    st.markdown(
        """
Algumas recursões repetem **muito** trabalho. O Fibonacci ingênuo recalcula os
mesmos valores sem parar e fica lento (exponencial):

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

**Memoização** guarda cada resultado num "caderninho" (cache) e o reaproveita —
o cálculo vira rápido (linear):

```python
memo = {}
def fib(n):
    if n < 2:
        return n
    if n in memo:                       # ja calculei? devolve o guardado
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

Em Python há um atalho pronto — um **decorador** que memoiza para você:

```python
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```
        """
    )

st.caption(
    "📖 **Documentação oficial do Python:** [Definindo funções](https://docs.python.org/pt-br/3/tutorial/controlflow.html#defining-functions) — uma função recursiva chama a si mesma."
)

st.info("Use os botões **‹ ›** no topo para navegar entre as fases.")

rodape_fases(__file__)
