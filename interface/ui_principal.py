# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

import time
import streamlit as st
from langchain.schema import HumanMessage, AIMessage


def configurar_pagina():
    st.set_page_config(
        page_title="Oráculo",
        page_icon="✨",
        initial_sidebar_state="expanded",
        layout="centered",
        menu_items={
            "Get help": "mailto:germanocastanho@proton.me",
            "Report a bug": "https://github.com/germanocastanho/oraculo/issues",
            "About": "https://github.com/germanocastanho/oraculo",
        },
    )


def inicializar_interface():
    fluxo = st.session_state.get("fluxo_conversacional")

    st.markdown(
        '<h1 style="text-align: center">Oráculo Acadêmico 🤖📚</h1>',
        unsafe_allow_html=True,
    )
    st.markdown("")

    return fluxo


def exibir_historico(fluxo):
    historico = fluxo.memory.chat_memory.messages
    conteudos_exibidos = set()

    for mensagem in historico:
        conteudo = str(mensagem.content)
        if conteudo not in conteudos_exibidos:
            conteudos_exibidos.add(conteudo)
            with st.chat_message(
                "user" if isinstance(mensagem, HumanMessage) else "assistant"
            ):
                st.markdown(conteudo)


def processar_mensagem(fluxo):
    pergunta = st.chat_input("Pergunte para o Oráculo ✨", key="input_usuario")
    if pergunta:
        fluxo.memory.chat_memory.add_message(HumanMessage(content=pergunta))
        with st.chat_message("user"):
            st.markdown(pergunta)

        with st.chat_message("assistant"):
            placeholder = st.empty()
            full_response = ""
            stream = fluxo.stream(
                input={"question": pergunta}, config={"callbacks": None}
            )

            response_text = ""
            for chunk in stream:
                if isinstance(chunk, dict):
                    response_text += chunk.get("answer", next(iter(chunk.values()), ""))
                else:
                    response_text += str(chunk)

            for char in response_text:
                full_response += char
                placeholder.markdown(full_response + "▌")
                time.sleep(0.03)

            placeholder.markdown(full_response)
            fluxo.memory.chat_memory.add_message(AIMessage(content=full_response))


def exibir_conversa():
    fluxo = inicializar_interface()
    if not fluxo:
        return

    exibir_historico(fluxo)
    processar_mensagem(fluxo)
