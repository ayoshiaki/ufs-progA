import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st
from utils.navegacao import legenda_fases, TOTAL_TEMAS

st.title("🐍 Programação A")
st.caption("Do pensamento computacional à orientação a objetos — um problema de cada vez.")

st.markdown(
    f"""
Bem-vindo! Este curso é feito de **problemas com dificuldade crescente**.
São **{TOTAL_TEMAS} temas**, e em cada um você não vai só assistir — vai
**prever, rodar, investigar, modificar e criar** código.
"""
)

st.markdown(
    f"""
### O método de ensino: PRIMM

Cada item do **menu lateral** é um dos {TOTAL_TEMAS} temas, e dentro de cada um
você percorre as mesmas **cinco fases**, sempre com os botões **‹ ›** no topo.
Essas fases seguem o método **PRIMM** — sigla, em inglês, de *Predict, Run,
Investigate, Modify, Make*, que aqui chamamos de **Prever, Rodar, Investigar,
Modificar e Criar**.

A premissa do PRIMM é que se aprende a programar **lendo e compreendendo código
antes de escrevê-lo do zero**. Em vez de encarar uma página em branco, você parte
de um programa que já funciona: primeiro **prevê** o que ele faz, depois o **roda**
para confirmar (ou se surpreender com) a previsão, **investiga** o *porquê* do
comportamento, faz pequenas **modificações** para mudar o resultado e, só então,
**cria** um programa novo — a tarefa que você entrega. Essa caminhada do ler para
o escrever distribui a dificuldade em passos curtos, reduz a sobrecarga de quem
está começando e dá segurança a cada etapa: as quatro primeiras fases são de
autocorreção (você vê na hora se acertou) e a última gera um **comprovante de
entrega**.

O PRIMM foi proposto por **Sue Sentance e Jane Waite** e fundamentado numa
perspectiva **sociocultural** da aprendizagem — na tradição de Vygotsky, em que a
linguagem e a mediação social precedem a construção individual do conhecimento —,
com evidências de ganho de aprendizado em sala de aula (Sentance, Waite e Kallia,
2019).
"""
)

legenda_fases()

st.caption(
    "**Referência:** SENTANCE, S.; WAITE, J.; KALLIA, M. *Teaching computer "
    "programming with PRIMM: a sociocultural perspective.* Computer Science "
    "Education, v. 29, n. 2–3, p. 136–176, 2019. "
    "DOI: [10.1080/08993408.2019.1608781](https://doi.org/10.1080/08993408.2019.1608781)."
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
