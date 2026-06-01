import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from utils import quiz as stb  # embaralha as alternativas dos quizzes
from utils.navegacao import mapa_curso, legenda_fases, TOTAL_TEMAS

st.title("🐍 Programação A")
st.caption("Do pensamento computacional à orientação a objetos — um problema de cada vez.")

st.markdown(
    f"""
Bem-vindo! Este curso é feito de **problemas com dificuldade crescente**.
São **{TOTAL_TEMAS} temas**, e em cada um você não vai só assistir — vai
**prever, rodar, investigar, modificar e criar** código.

### Os {TOTAL_TEMAS} temas do curso
"""
)

mapa_curso()

st.markdown(
    f"""
Cada item do **menu lateral** é um desses {TOTAL_TEMAS} temas. Dentro dele, você
avança pelas mesmas **5 fases** com os botões **‹ ›** no topo.

### As 5 fases de cada tema (PRIMM)
"""
)

legenda_fases()

st.markdown(
    """
### O que você faz em cada fase
1. **🔮 Prever** — leia um trecho de código e adivinhe o que ele faz, *antes* de rodar.
2. **▶️ Rodar** — execute e confira se sua previsão estava certa.
3. **🔍 Investigar** — responda perguntas sobre *por que* o código se comporta assim.
4. **🔧 Modificar** — altere o código para mudar o comportamento.
5. **🛠️ Criar** — resolva um problema novo do zero. **Esta é a tarefa que você entrega.**

As fases 1–4 são curtas e de autocorreção (clique e veja na hora se acertou).
A fase 5 gera um **comprovante de entrega** para você anexar onde o professor indicar.

### Regras do jogo
- Tente prever **antes** de rodar — é aí que o aprendizado acontece.
- Errar é parte do processo: os testes existem para te dar pistas, não nota.
- Só avance de tema quando fechar a fase **Criar**.
"""
)

stb.to_do_list(
    {
        "Tenho Python 3.10+ instalado (ou vou usar o app na nuvem)": False,
        "Sei abrir e rodar este livro": False,
        "Entendi as 5 fases de cada tema": False,
        "Sei onde entregar o comprovante da fase Criar": False,
    },
    header="### ✅ Checklist antes de começar",
    success="Tudo pronto. Bora para o Tema 1!",
)

st.divider()
st.subheader("🤖 Sobre o uso de IA neste material")
st.info(
    "Este material é **baseado nas aulas de Programação A lecionadas pelo "
    "Prof. Dr. André Yoshiaki Kashiwabara**. A IA **Claude Opus 4.8** (Anthropic) "
    "foi usada para **formatar e estruturar esse conteúdo no sistema interativo "
    "(Streamlit)**. A **revisão final e a responsabilidade pelo conteúdo são do "
    "professor** — a IA é um instrumento de apoio, não autora."
)
st.markdown(
    """
**Como a IA foi usada:** partindo das **aulas lecionadas pelo professor**, para
**formatar o conteúdo no sistema Streamlit** — organizar cada tema nas cinco
fases (PRIMM), redigir os exemplos e quizzes e montar a navegação. Todo o
material foi **revisado, testado e ajustado pelo professor** antes de publicar.

Divulgar o uso de IA faz parte de um compromisso com **transparência, ética e
responsabilidade** — os mesmos princípios que se espera de você. Ao usar IA nos
seus próprios trabalhos, **declare o uso** (ferramenta, versão e como ela
ajudou) e siga as orientações da sua instituição:

- **USP** — [repositório de diretrizes de uso de IA no ensino](https://understandingai.iea.usp.br/guidelines-para-o-uso-da-ia-no-ensino/),
  mantido pelo IEA-USP.
- **UFS** — guia [*Educar com Inteligência Artificial*](https://www.ufs.br/conteudo/78564-ufs-e-seduc-lancam-guia-sobre-uso-responsavel-da-inteligencia-artificial-na-educacao)
  (UFS em parceria com a Seduc/SE), sobre o uso responsável de IA na educação.

*As diretrizes institucionais sobre IA ainda estão em evolução — consulte sempre
a versão vigente na sua universidade.*
"""
)

st.divider()
st.subheader("🔒 Privacidade e seus dados")
st.markdown(
    """
Este material respeita a sua privacidade e os princípios da **LGPD**. O que é
coletado e para quê:

- **Nome e matrícula** — pedidos apenas na fase **Criar**, para gerar o
  **comprovante de entrega**. Entram somente no arquivo `.txt` que **você
  baixa**; este app **não os armazena em servidor**.
- **Respostas dos quizzes** — podem ser **salvas** e vinculadas a um
  **identificador (token)** pelo cartão *💾 Salvar progresso* da barra lateral,
  para você **retomar de onde parou**. Guarde o link com cuidado: **quem tiver o
  link vê esse progresso**.

**Finalidade:** registrar a entrega das tarefas e permitir retomar o progresso.
Os dados **não são vendidos nem compartilhados** com terceiros.

**Seus direitos (LGPD):** para dúvidas, correção ou exclusão dos seus dados,
procure o **professor responsável pela disciplina**.
"""
)
