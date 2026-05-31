# Design — Navegação "Bússola do curso"

Data: 2026-05-31

## Objetivo

Tornar a navegação do livro Programação A mais fácil: o aluno sempre sabe
**onde está** (tema/fase), **o que vem depois** e **o tamanho do curso**.

## Restrições verificadas (streamlit_book 0.7.6)

- App de **página única**: `streamlit_app.py` roda sempre; a sidebar
  (`option_menu`) escolhe o capítulo e `page_number` em `session_state` escolhe
  o arquivo. → `st.page_link`/`st.navigation`/`st.tabs` **não** servem para pular
  entre fases (confirmado em book_config.py / chapter_config.py / file_reader.py).
- `set_book_config` só repassa ao componente: `options, menu_title, menu_icon,
  icons, orientation, styles, display_page_info, save_answers`. `toc`, `button*`,
  `on_load_*` ficam nos defaults (não dá para setá-los pelo app).
- `styles` aceita 4 chaves: `container`, `icon`, `nav-link`, `nav-link-selected`.
- `display_page_info=False` remove a legenda `"Page X of Y. File: <caminho>"`
  (confirmado em file_reader.py:48 — `if display_page_info: st.caption(...)`).
- A sidebar é 100% ocupada pelo `option_menu`; legenda extra cairia abaixo
  (descartado). CSS `position:sticky` para cabeçalho fixo é frágil (descartado).

## Componentes

### 1. `utils/navegacao.py` (novo) — fonte única
Mapas únicos `TEMAS` (1→10, nomes sem prefixo numérico, espelhando
`streamlit_app.py`) e `FASES` (1→5, emoji+nome). Deriva tema/fase do `__file__`:
`_tema` lê `Path(arquivo).parent.name` (`02_tipos`→2); `_fase` lê o stem
(`03_investigar`→3, `00_intro`→0). Funções públicas:

- `cabecalho(arquivo)` — fases 1–5: `st.caption("Tema N · Nome")` (breadcrumb) +
  **trilha PRIMM** via `st.columns(5)` (emoji + nome de cada fase; a atual em
  **negrito**, as demais em `:gray[...]`) + `st.caption("Fase X de 5")` + divider.
  Sem HTML cru — usa a sintaxe de cor nativa do markdown do Streamlit.
- `cabecalho_intro(arquivo)` — fase 0: `st.caption("Tema N de 10")` +
  `st.title("Tema N · Nome")` + `st.subheader("Fase 0 — Aquecimento")`.
- `rodape_tema(arquivo)` — `st.success` "Tema N de 10 concluído… siga para o
  Tema N+1 · Nome"; no Tema 10, mensagem de fim de curso.
- `mapa_curso()` — grade 2×5 dos 10 temas (`st.columns`).
- `legenda_fases()` — fila das 5 fases PRIMM (`st.columns(5)`).

### 2. Cabeçalho nas 60 páginas
- 10 `00_intro.py`: título+subheader → `cabecalho_intro(__file__)`.
- 50 fases (01–05): `st.subheader("Fase N — …")` → `cabecalho(__file__)`.
- 10 `05_criar.py`: `rodape_tema(__file__)` como última linha.
- Páginas sem o bootstrap `sys.path` (00_intro, 01_prever, 03_investigar)
  recebem as 3 linhas no topo + o import de `utils.navegacao`.

### 3. `pages/00_boas_vindas.py`
Após o markdown das 5 fases: `mapa_curso()` + `legenda_fases()`; texto ajustado
para citar "10 temas". Mantém o `stb.to_do_list` existente.

### 4. `streamlit_app.py`
`stb.set_book_config(..., display_page_info=False, styles={...})` — esconde o
caminho do arquivo e destaca o capítulo ativo na sidebar (4 chaves permitidas).

## Sequência
1. `utils/navegacao.py` + teste isolado das funções `_tema`/`_fase` com caminhos simulados.
2. `streamlit_app.py` (display_page_info + styles).
3. `boas_vindas.py` (mapa + legenda + "10 temas").
4. Transformar as 60 páginas via script determinístico; piloto no Tema 2, depois propagar.
5. `rodape_tema` nas 10 fases Criar (caso especial Tema 10).
6. Verificação: py_compile; AppTest (0 exceções) navegando os temas; spot-check visual.

## Fora de escopo
- Stepper com CSS por span; legenda fixa na sidebar; bloquear avanço sem
  completar Criar; migrar `components.html`→`st.iframe` (deprecação separada).
