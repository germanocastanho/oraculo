# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

import os
import time
import streamlit as st
from interface.estado_sessao import preparar_estado_sessao, salvar_configuracoes
from logica.logica_chat import criar_fluxo_conversacao
from logica.modelos import MODELOS


def exibir_campo_modelo():
    nomes_modelos = {k: f"{k} - Modelo {v['caractere']}" for k, v in MODELOS.items()}
    modelo_padrao = st.session_state["config"].get(
        "modelo", list(nomes_modelos.keys())[0]
    )
    st.session_state["config"]["modelo"] = st.selectbox(
        "**Escolha a *inteligência artificial***:",
        options=list(nomes_modelos.keys()),
        format_func=lambda x: nomes_modelos[x],
        index=list(nomes_modelos.keys()).index(modelo_padrao),
    )


def exibir_campo_chave():
    chave = st.text_input(
        "**Insira a *chave API*** correspondente:",
        type="password",
        value=st.session_state["config"].get("chave", ""),
    )
    if chave:
        st.session_state["config"]["chave"] = chave


def exibir_campo_diretorio():
    diretorio = st.text_input(
        "**Insira a pasta com *Markdowns***:",
        value=st.session_state["config"].get("diretorio", ""),
    )
    if diretorio:
        st.session_state["config"]["diretorio"] = diretorio


def validar_configuracoes():
    config = st.session_state["config"]
    modelo = config.get("modelo")
    chave = config.get("chave", "").strip()
    diretorio = config.get("diretorio")

    if not modelo:
        return "Por favor, selecione um modelo válido! ❌"

    if not chave or len(chave) < 50:
        return "Por favor, insira uma chave API válida! ❌"

    if (
        not diretorio
        or not os.path.isdir(diretorio)
        or not [f for f in os.listdir(diretorio) if f.endswith(".md")]
    ):
        return "Por favor, insira uma pasta válida! ❌"

    return None


def exibir_botoes():
    mensagem_erro = validar_configuracoes()

    if st.button("Configurar Oráculo 🚀", use_container_width=True):
        if not mensagem_erro:
            with st.spinner("Configurando o Oráculo..."):
                criar_fluxo_conversacao()
                st.session_state["oraculo_inicializado"] = True
            st.markdown(
                f'<p style="text-align: center">Oráculo configurado com sucesso! 🚀</p>',
                unsafe_allow_html=True,
            )
            time.sleep(3)
            st.rerun()
        else:
            st.markdown(
                f'<p style="text-align: center">{mensagem_erro}</p>',
                unsafe_allow_html=True,
            )

    if st.session_state.get("oraculo_inicializado"):
        if st.button("Limpar conversa 🗑️", use_container_width=True):
            with st.spinner("Limpando a conversa..."):
                st.session_state["fluxo_conversacional"].memory.chat_memory.clear()
            st.markdown(
                f'<p style="text-align: center">Conversa limpa com sucesso! 🚀</p>',
                unsafe_allow_html=True,
            )
            time.sleep(3)
            st.rerun()


def exibir_configuracoes():
    with st.sidebar:
        st.markdown(
            '<h1 style="text-align: center">Configurações ⚙️</h1>',
            unsafe_allow_html=True,
        )
        st.markdown("")
        preparar_estado_sessao()
        exibir_campo_modelo()
        exibir_campo_chave()
        exibir_campo_diretorio()
        salvar_configuracoes(st.session_state["config"])
        exibir_botoes()
