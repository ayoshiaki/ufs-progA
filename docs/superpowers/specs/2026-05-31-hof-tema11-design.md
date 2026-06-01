# Tema 11 · Funções de ordem superior (HOF) — design

**Data:** 2026-05-31
**Status:** aprovado

## Objetivo

Adicionar um novo tema ao livro interativo *Programação A*, sobre **funções de
ordem superior (HOF)**, fechando o curso com a ideia de que **funções são
valores** que podem ser passados como argumento. O tema entra como **Tema 11**,
no fim (depois de Herança), sem renomear nenhuma pasta existente.

## Escopo

**Dentro:** função-como-argumento (passar uma função para outra) e `lambda`
como notação curta de função sem nome.

**Fora (YAGNI):** `map`, `filter`, `sorted(key=)`/`max(key=)` e closures —
recorte mínimo escolhido para fechar o curso sem sobrecarregar.

## Contexto da arquitetura

- O livro usa o método **PRIMM**: cada tema é uma pasta `NN_nome/` com 6
  arquivos de fase (`00_intro`, `01_prever`, `02_rodar`, `03_investigar`,
  `04_modificar`, `05_criar`).
- Convenção sobre configuração: a pasta define o tema e o prefixo do arquivo
  define a fase (`utils/navegacao.py` deriva tudo do caminho).
- Título, ícone e ordem de cada tema vivem em **duas fontes-espelho** que
  precisam ser mantidas em sincronia: `streamlit_app.py` e `utils/navegacao.py`.
- `TOTAL_TEMAS` é derivado de `len(TEMAS)`; logo, `cabecalho_intro`,
  `rodape_tema` e afins se ajustam sozinhos ao crescer o dicionário `TEMAS` —
  exceto textos com o número "10" escrito à mão.

## Decisão técnica — fase Criar

Há duas variantes de sandbox Pyodide (client-side) para a fase Criar:

- `exercicio_funcao_sandbox` — passa `args` como **JSON**; **não serializa
  funções**, então não serve para HOF.
- `exercicio_expressoes_sandbox` — cada caso é um **trecho de código** que
  termina atribuindo a `_res`; o esperado é comparado com `_res`. Permite
  passar uma `lambda` para a função do aluno.

Portanto a fase Criar do Tema 11 usa **`exercicio_expressoes_sandbox`**, o mesmo
mecanismo já usado nos Temas 9 e 10 (que testam classes).

## Conteúdo das 6 fases

Cabeçalho-padrão idêntico aos demais temas (`sys.path` para a raiz, imports de
`utils.navegacao`, `cabecalho`/`cabecalho_intro` + `rodape_fases`/`rodape_tema`).

| Fase | Arquivo | Conteúdo |
|---|---|---|
| 0 Aquecimento | `00_intro.py` | Problema: o mesmo laço repetido mudando só "o que fazer com cada item"; solução: passar **a ação como argumento**. Funções são valores. Apresenta `lambda` como função curta sem nome. Pergunta-isca ("pense antes de avançar"). |
| 1 Prever | `01_prever.py` | Ler **sem rodar** `def aplicar(f, x): return f(x)` chamado com uma função nomeada; e um caso com `lambda`. `stb.true_or_false` + `stb.single_choice`. |
| 2 Rodar | `02_rodar.py` | Confirmar a previsão rodando (`exercicio_saida`). Observação: o parâmetro `f` *guarda uma função*; chamar `f(x)` executa a função recebida. |
| 3 Investigar | `03_investigar.py` | O *porquê*: por que passar a função em vez de copiar o laço? `stb.single_choice` + `stb.multiple_choice` sobre função-como-valor e `lambda`. |
| 4 Modificar | `04_modificar.py` | Dada `aplicar_a_todos(funcao, lista)` que usa uma operação fixa, trocar para usar o parâmetro `funcao` (ou um `lambda`). `exercicio_saida` com saída esperada determinística. |
| 5 Criar | `05_criar.py` | Aluno escreve uma HOF própria — `aplicar(funcao, valor)` que devolve `funcao(valor)`. Testada via `exercicio_expressoes_sandbox`, casos como `_res = aplicar(lambda x: x + 1, 10)` → `11`. `nome_tarefa="tema11_aplicar"`. Fecha com `rodape_fases` + `rodape_tema`. |

Tom e formato seguem o Tema 7 (Funções): markdown em português, exemplos
curtos, feedbacks `success`/`error` explicativos.

## Registro do tema (fontes-espelho)

`streamlit_app.py`:
- `options`: acrescentar `"11 · Funções de ordem superior"`.
- `paths`: acrescentar `current / "11_hof"`.
- `icons`: acrescentar um ícone bootstrap (ex.: `"arrow-right-circle"`).

`utils/navegacao.py`:
- `TEMAS[11] = "Funções de ordem superior"`.
- `TOTAL_TEMAS` deriva de `len(TEMAS)` — nada a mudar na lógica.

## Textos "10 → 11" e grid

- `utils/navegacao.py` (~linha 125): mensagem final de `rodape_tema`
  "completou os **10** temas" → **11**.
- `utils/navegacao.py` `mapa_curso`: generalizar o grid (hoje fixo em 2×5,
  `numeros[:5]`/`numeros[5:]`) para **não perder o 11º tema** — quebrar a lista
  em faixas de tamanho fixo (ex.: 5 por linha) e dimensionar `st.columns` pelo
  tamanho da faixa.
- `pages/00_boas_vindas.py`: três menções a "10 temas" (linhas ~15, 18, 26).
- `README.md`: duas menções (linhas ~14, 46) — documentação.

## Fora de escopo

- Sem entrada nova em `grading_endpoint/gabarito.py`: a sandbox corrige no
  navegador; o endpoint de correção é um deploy separado e opcional, e hoje só
  cobre um subconjunto das tarefas.

## Critérios de sucesso

1. O Tema 11 aparece no menu lateral, com ícone, depois do Tema 10.
2. As 6 fases navegam corretamente com os botões ‹ › e com os botões de rodapé.
3. A fase Criar roda na sandbox, passa nos casos com `lambda` e libera o
   comprovante `tema11_aplicar`.
4. `rodape_tema` na fase Criar do Tema 11 mostra a mensagem final de conclusão
   do curso (ramo `t == TOTAL_TEMAS`) já com "11 temas".
5. Nenhum texto remanescente diz "10 temas" onde agora são 11.
6. O `mapa_curso` na página de boas-vindas mostra os 11 temas sem cortar o 11º.
