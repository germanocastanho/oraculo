# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

import os
import json
import streamlit as st

CAMINHO_CONFIG = "config.json"


def carregar_configuracoes():
    if not os.path.exists(CAMINHO_CONFIG):
        return {}
    with open(CAMINHO_CONFIG) as arquivo:
        return json.load(arquivo)


def salvar_configuracoes(config):
    with open(CAMINHO_CONFIG, "w") as arquivo:
        json.dump(config, arquivo)


def preparar_estado_sessao():
    for chave, valor in {
        "config": carregar_configuracoes(),
        "fluxo_conversacional": None,
        "indice_pronto": False,
        "erros": [],
        "historico_interacoes": [],
    }.items():
        st.session_state.setdefault(chave, valor)


def resetar_fluxo_conversacional():
    st.session_state.update(
        {
            "fluxo_conversacional": None,
            "historico_interacoes": [],
            "indice_pronto": False,
            "erros": [],
        }
    )