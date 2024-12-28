# Copyleft 🄯, Germano Castanho, 2024
# Software livre licenciado sob a GPL-3.0
# Cada linha, um manifesto pela liberdade

import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationalRetrievalChain
from logica.modelos import carregar_modelo
from logica.indexador_docs import gerar_resumos_markdown
from logica.indexador_docs import criar_indice_vetorial


def criar_fluxo_conversacao():
    config = st.session_state["config"]
    modelo = carregar_modelo(config["modelo"], config["chave"])

    if not modelo:
        return

    resumos = gerar_resumos_markdown(
        modelo,
        config["diretorio"],
        """
        #### INSTRUÇÃO:
            
        Resuma o conteúdo do corpus fornecido de forma clara, objetiva e concisa. O resumo deve capturar as ideias principais e os tópicos centrais do texto, sem incluir interpretações ou especulações. 

        #### DIRETRIZES:

        - Extraia apenas as informações essenciais do texto, mantendo a fidelidade ao conteúdo original.
        - O resumo deve ser estruturado como um único parágrafo ou uma série de frases curtas e coesas.
        - Evite repetir informações ou usar linguagem redundante.
        - Sempre mantenha o tom técnico e informativo, adequado para indexação em um sistema vetorial.

        #### CONTEXTO:

        - **Texto a ser resumido:** {context}

        #### RESUMO:
        """,
    )
    indice = criar_indice_vetorial(list(resumos.values()))

    prompt = PromptTemplate.from_template(
        """
        #### PERSONA:
 
        Você é o **Oráculo**, um assistente acadêmico especializado em pesquisa e gerenciamento de informações extraídas de arquivos Markdown, armazenados em cofres do Obsidian. Seu objetivo é auxiliar o usuário a explorar, compreender e sintetizar informações relevantes do corpus fornecido.
       
        #### DIRETRIZES:
       
        - Responda exclusivamente com base no **contexto fornecido**, mantendo total fidelidade às informações disponíveis no corpus. Evite especulações ou informações não fundamentadas.
        - Caso o contexto não contenha dados suficientes, indique isso claramente e sugira alternativas, como o refinamento da pergunta do usuário ou a revisão do corpus.
        - Use um **tom acadêmico e técnico**, estruturando respostas em parágrafos coesos e claros.
        - Sempre que possível, **cite diretamente** trechos ou ideias do corpus para embasar suas respostas, garantindo rastreabilidade e precisão.
        - Ofereça respostas completas e objetivas, evitando redundâncias e repetições desnecessárias.

        #### INTERAÇÃO:

        - **Contexto fornecido:** {context}
        - **Histórico da conversa:** {chat_history}
        - **Pergunta do usuário:** {question}

        #### RESPOSTA:                      
        """
    )

    st.session_state["fluxo_conversacional"] = ConversationalRetrievalChain.from_llm(
        llm=modelo,
        memory=ConversationBufferMemory(
            memory_key="chat_history", return_messages=True
        ),
        retriever=indice.as_retriever(
            search_type="similarity", search_kwargs={"fetch_k": 20, "k": 7}
        ),
        verbose=True,
        combine_docs_chain_kwargs={"prompt": prompt},
        output_key="answer",
    )
