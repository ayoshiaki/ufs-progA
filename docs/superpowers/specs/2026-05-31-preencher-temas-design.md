# Design — Preencher os 8 temas faltantes

Data: 2026-05-31

## Objetivo

Completar os 8 temas que hoje são placeholders (`00_em_construcao.py`),
seguindo o método PRIMM em 5 fases já estabelecido nos Temas 1 e 4.

Temas a preencher: 2 (Tipos), 3 (Condicionais), 5 (Coleções), 6 (Strings),
7 (Funções), 8 (Arquivos/erros), 9 (Objetos), 10 (Herança).

## Padrão por tema

Cada pasta `pages/NN_tema/` substitui `00_em_construcao.py` por 6 arquivos:

| Arquivo | Fase | Componente |
|---|---|---|
| `00_intro.py` | Aquecimento | markdown (título + problema do tema) |
| `01_prever.py` | 🔮 Prever | `stb.true_or_false` + `stb.single_choice` |
| `02_rodar.py` | ▶️ Rodar | `exercicio_saida` (exec servidor, **sem `input()`**) |
| `03_investigar.py` | 🔍 Investigar | `stb.single_choice` + `stb.multiple_choice` |
| `04_modificar.py` | 🔧 Modificar | `exercicio_saida` |
| `05_criar.py` | 🛠️ Criar | Pyodide (sandbox WASM) + comprovante |

Fases 2 e 4 usam valores fixos no código (nunca `input()`), como o modelo,
para contornar a limitação do autograder server-side.

## Conteúdo / entrega por tema

| # | Tema | Entrega (fase 5) | Casos |
|---|---|---|---|
| 2 | Tipos/expressões | `celsius_para_fahrenheit(c)` | 0→32, 100→212, 20→68, −40→−40, 25→77 (todos exatos em float) |
| 3 | Condicionais | `situacao(media)` | ≥7 "Aprovado"; 5≤m<7 "Recuperação"; <5 "Reprovado" |
| 5 | Coleções | `buscar_telefone(agenda, nome)` | dict→telefone; ausente→"não encontrado" |
| 6 | Strings | `eh_palindromo(texto)` | ignora maiúsc./espaços; arara→True, casa→False |
| 7 | Funções | `total_compra(preco, qtd, desconto)` | inteiros (sem float) |
| 8 | Arquivos/erros | `media_notas(linhas)` | lista de strings; try/except ignora inválidos |
| 9 | Objetos | classe `ContaBancaria` | depositar/sacar/saldo |
| 10 | Herança | `Forma`/`Circulo`/`Retangulo` | `.area()` |

## Restrições técnicas e decisões

1. **OO (temas 9 e 10) entregam classes, não funções.** O
   `exercicio_funcao_sandbox` só faz `func(*args) == esperado`. Adicionar um
   helper **aditivo** `exercicio_expressoes_sandbox(...)` em
   `utils/sandbox_pyodide.py`: executa o código do aluno e avalia uma lista de
   **expressões** (`"c = ContaBancaria(100); c.sacar(30); _res = c.saldo"` → `70`)
   contra o esperado. Não altera o helper existente.

2. **Tema 8 lê arquivo, mas o Pyodide não tem o arquivo no servidor.**
   Reformular a entrega para `media_notas(linhas)` (lista de strings já lidas),
   usando `try/except` para ignorar valores inválidos. As fases 0–4 ainda
   ensinam `with open`/`except`; só a entrega opera sobre dados em memória.

3. **Float exato:** escolher casos de teste com resultados exatos em ponto
   flutuante (evita falha por `==` no Pyodide). Tema 2 usa apenas valores cujo
   resultado é inteiro/exato; Tema 10 testa área com `round(...)`.

## Fora de escopo (rodada futura)

- Bug do `input()`/`sys.stdin` em `utils/autograder.py` (contornado: sem `input()`).
- Inconsistência `==` (exec) vs `canon()` (endpoint remoto).
- Preencher o `gabarito.py` do endpoint remoto para os novos temas.

## Verificação

- `python -m py_compile` em todos os arquivos novos.
- Simulação dos runners Pyodide (função e expressões) com soluções de
  referência → `ok_all=True` nos 8 temas.
- Execução de todas as 62 páginas com streamlit/streamlit_book mockados → 0 erros.
- HTML gerado pelos dois helpers Pyodide: JSON válido, sem placeholders `$`.
