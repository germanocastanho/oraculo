# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq

MODELOS = {
    "ChatGPT": {
        "nome": "ChatGPT 4o",
        "classe": ChatOpenAI,
        "id_modelo": "gpt-4o",
        "caractere": "avançado e robusto",
    },
    "Llama": {
        "nome": "Llama 3.3",
        "classe": ChatGroq,
        "id_modelo": "llama-3.3-70b-versatile",
        "caractere": "gratuito e open source",
    },
}


def carregar_modelo(nome_modelo, chave_api):
    modelo_escolhido = MODELOS.get(nome_modelo)
    return modelo_escolhido["classe"](
        model=modelo_escolhido["id_modelo"],
        api_key=chave_api,
        temperature=0.2,
        top_p=0.8,
        max_tokens=1000,
    )
