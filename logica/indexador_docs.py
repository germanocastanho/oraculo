# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

import os
import concurrent.futures
from langchain.schema import HumanMessage
from langchain_community.vectorstores.faiss import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


def gerar_resumos_markdown(modelo, diretorio, mensagem):
    def resumir_arquivo(arquivo):
        if not arquivo.endswith(".md"):
            return None

        abrir_arquivo = os.path.join(diretorio, arquivo)
        with open(abrir_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read()

        prompt = f"""
        #### INSTRUÇÃO:

        Com base na **mensagem do usuário**, elabore um resumo do conteúdo fornecido em até **1000 caracteres**. O resumo deve ser objetivo, capturando as informações mais relevantes relacionadas à mensagem do usuário, sem adicionar interpretações ou informações externas.

        #### CONTEÚDO:
        
        **Texto a ser resumido:** {conteudo}

        #### MENSAGEM:

        **Mensagem do usuário:** {mensagem}

        #### RESUMO:
        """

        resumo = modelo.invoke([HumanMessage(content=prompt)]).content
        return (arquivo, resumo[:1000] if len(resumo) > 1000 else resumo)

    resumos = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for resultado in executor.map(resumir_arquivo, os.listdir(diretorio)):
            if resultado:
                resumos[resultado[0]] = resultado[1]

    return resumos


def criar_indice_vetorial(lista_de_resumos):
    return FAISS.from_texts(
        texts=lista_de_resumos,
        embedding=HuggingFaceEmbeddings(model_name="all-mpnet-base-v2"),
    )
