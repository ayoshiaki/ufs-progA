"""
Componentes de interface reutilizáveis nas páginas do livro.

Importe assim dentro de uma página:
    from utils.componentes import exercicio_funcao, exercicio_saida, comprovante
"""

import datetime
import hashlib
import streamlit as st

from utils.autograder import check_function, check_output, run_code


def _resultados_tabela(resultados):
    linhas = []
    for r in resultados:
        marca = "✅" if r["ok"] else "❌"
        linhas.append({
            "": marca,
            "entrada": str(r["args"]),
            "esperado": str(r["esperado"]),
            "obtido": str(r["obtido"]),
        })
    st.dataframe(linhas, hide_index=True, use_container_width=True)


def exercicio_funcao(chave, enunciado, func_name, cases, modelo="", dica=""):
    """Tarefa em que o aluno implementa uma função e ela é testada."""
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)
    codigo = st.text_area(
        "Seu código:", value=modelo, height=220, key=f"code_{chave}",
    )
    if st.button("Rodar e verificar", key=f"btn_{chave}"):
        passou, resultados = check_function(codigo, func_name, cases)
        _resultados_tabela(resultados)
        if passou:
            st.success("🎉 Todos os testes passaram! Tarefa concluída.")
            st.session_state[f"ok_{chave}"] = codigo
        else:
            primeiro_erro = next((r for r in resultados if r.get("erro")), None)
            if primeiro_erro and primeiro_erro["erro"]:
                st.code(primeiro_erro["erro"], language="text")
            st.warning("Ainda não passou em todos os casos. Ajuste e tente de novo.")
    return st.session_state.get(f"ok_{chave}")


def exercicio_saida(chave, enunciado, esperado, modelo="", stdin_text="", dica=""):
    """Tarefa em que o aluno escreve um programa cuja SAÍDA é verificada."""
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)
    codigo = st.text_area(
        "Seu código:", value=modelo, height=200, key=f"code_{chave}",
    )
    if st.button("Rodar e verificar", key=f"btn_{chave}"):
        ok, saida, erro = check_output(codigo, esperado, stdin_text)
        st.markdown("**Saída do seu programa:**")
        st.code(saida or "(sem saída)", language="text")
        if erro:
            st.code(erro, language="text")
        if ok:
            st.success("🎉 Saída correta! Tarefa concluída.")
            st.session_state[f"ok_{chave}"] = codigo
        else:
            st.warning("A saída ainda não bate com o esperado.")
    return st.session_state.get(f"ok_{chave}")


def comprovante(nome_tarefa, codigo_aluno):
    """
    Gera um comprovante de entrega baixável (texto) com hash + carimbo de tempo.
    Use no fim de uma fase 'Criar' para o aluno anexar na entrega.
    """
    if not codigo_aluno:
        st.info("Conclua o exercício acima (todos os testes verdes) para liberar o comprovante.")
        return
    nome = st.text_input("Seu nome completo:", key=f"nome_{nome_tarefa}")
    matricula = st.text_input("Matrícula:", key=f"mat_{nome_tarefa}")
    if nome and matricula:
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        assinatura = hashlib.sha256(
            f"{matricula}{codigo_aluno}{agora}".encode()
        ).hexdigest()[:12]
        conteudo = (
            f"COMPROVANTE DE ENTREGA — Programação A\n"
            f"Tarefa: {nome_tarefa}\n"
            f"Aluno: {nome}\nMatrícula: {matricula}\n"
            f"Data/hora: {agora}\nAssinatura: {assinatura}\n"
            f"{'-' * 50}\n{codigo_aluno}\n"
        )
        st.download_button(
            "📄 Baixar comprovante de entrega",
            data=conteudo,
            file_name=f"entrega_{nome_tarefa}_{matricula}.txt",
            mime="text/plain",
            key=f"dl_{nome_tarefa}",
        )
