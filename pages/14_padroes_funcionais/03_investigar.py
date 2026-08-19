import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from utils import quiz as stb
from utils.navegacao import cabecalho, rodape_fases

cabecalho(__file__)
st.markdown("Agora o *porquê* de cada padrão.")

stb.single_choice(
    "Por que preferir uma **tabela de despacho** (`dict` de nome→função) a um "
    "`if/elif` comprido?",
    [
        "Para adicionar uma ação nova basta uma entrada no dict — sem mexer na lógica e sem risco de esquecer um `elif`.",
        "Porque `dict` deixa o programa mais rápido em qualquer situação.",
        "Porque `if/elif` não consegue chamar funções.",
        "Só por estética; não muda nada na prática.",
    ],
    0,
    success="Isso! A tabela separa *quais* ações existem de *como* escolher uma — fica fácil estender e difícil esquecer um caso.",
    error="A vantagem é organização e extensibilidade: novas ações entram como dados (uma chave no dict), não como mais um ramo no `if/elif`.",
)

st.divider()

stb.single_choice(
    "O que `partial(soma, 10)` faz **no momento em que é chamada**?",
    [
        "Devolve uma nova função com `a=10` já fixo; a soma só acontece quando essa função for chamada depois.",
        "Calcula `soma(10)` na hora e devolve o número.",
        "Modifica a função `soma` original para sempre usar 10.",
        "Dá erro, porque falta o segundo argumento.",
    ],
    0,
    success="Isso! `partial` apenas *prepara* a função fixando argumentos; o cálculo é adiado para a chamada.",
    error="`partial` não executa nada ainda — só devolve uma função com parte dos argumentos preenchidos, para chamar mais tarde.",
)

st.divider()

stb.single_choice(
    "Qual problema o **trampoline** resolve?",
    [
        "Recursão muito profunda estoura a pilha (`RecursionError`); o trampoline troca as chamadas empilhadas por um laço que 'quica' nos próximos passos.",
        "Funções que não devolvem nada.",
        "Erros de digitação no nome da função.",
        "Listas grandes demais para a memória.",
    ],
    0,
    success="Isso! Devolvendo 'o próximo passo' em vez de chamar a si mesma, a recursão vira um laço — sem empilhar chamadas.",
    error="O trampoline ataca o estouro de pilha: em vez de a função chamar a si mesma (empilhando), ela devolve o próximo passo e um laço o executa.",
)

st.divider()

stb.multiple_choice(
    "Sobre **pipe / composição**, marque o que é verdadeiro:",
    {
        "A saída de uma função vira a entrada da próxima.": True,
        "A ordem das funções importa para o resultado.": True,
        "Cada função do pipe precisa saber quais são as outras.": False,
        "Só funciona se todas as funções forem `lambda`.": False,
    },
    success="Isso! No pipe, o dado flui em ordem por funções independentes — cada uma só transforma o que recebe.",
    error="No pipe a ordem importa e o dado flui de uma para a próxima; mas as funções são independentes (não precisam se conhecer) e podem ter nome ou ser `lambda`.",
)

rodape_fases(__file__)
