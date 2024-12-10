#  Copyleft (C), Germano Castanho, 2024
#  Software livre licenciado sob a GPL-3.0.

import os
import re
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

config_modelos = {
    'Groq': {
        'modelos': [
            'llama-3.1-70b-versatile',
            'gemma2-9b-it',
            'mixtral-8x7b-32768'
        ],
        'chat': ChatGroq
    }
}

def markdown_para_texto(markdown_text):
    markdown_text = re.sub(r'^#+\s', '', markdown_text, flags=re.MULTILINE)
    markdown_text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', markdown_text)
    markdown_text = re.sub(r'(\*|_)(.*?)\1', r'\2', markdown_text)
    markdown_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown_text)
    markdown_text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', '', markdown_text)
    markdown_text = re.sub(r'```.*?```', '', markdown_text, flags=re.DOTALL)
    markdown_text = re.sub(r'`([^`]*)`', r'\1', markdown_text)
    markdown_text = re.sub(r'[>*#]', '', markdown_text)
    markdown_text = re.sub(r'\n{2,}', '\n', markdown_text)
    return markdown_text.strip()

def carrega_markdown(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        return markdown_para_texto(conteudo)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")
        return ''

def limitar_texto(texto, max_chars):
    return texto[:max_chars]

def carrega_cofre(caminho_diretorio, limite_arquivos=10, limite_chars=6000):
    documentos = []
    chars_por_arquivo = limite_chars // limite_arquivos
    for root, _, files in os.walk(caminho_diretorio):
        md_files = [f for f in files if f.endswith('.md')]
        for file in md_files[:limite_arquivos]:
            caminho_arquivo = os.path.join(root, file)
            conteudo = carrega_markdown(caminho_arquivo)
            texto_limitado = limitar_texto(conteudo, chars_por_arquivo)
            if texto_limitado:
                documentos.append(f"Arquivo: {file}\n\n{texto_limitado}")
    texto_final = "\n\n".join(documentos)
    return limitar_texto(texto_final, limite_chars)

def carrega_modelo(modelo, api_key, caminho_diretorio):
    if not os.path.isdir(caminho_diretorio):
        st.error(f"O diretório {caminho_diretorio} não existe.")
        st.stop()
    documentos = carrega_cofre(caminho_diretorio)
    if not documentos:
        st.error("Nenhum arquivo Markdown foi encontrado ou o conteúdo está vazio.")
        st.stop()
    system_message = (
        f"Você é um assistente acadêmico chamado Oráculo.\n"
        f"Você possui acesso às seguintes informações vindas do cofre Obsidian:\n\n"
        f"####\n{documentos}\n####\n\n"
        "Utilize as informações fornecidas para basear as suas respostas.\n"
        "Sempre que houver $ na sua saída, substitua por S.\n"
        'Se a informação do documento for algo como "Just a moment...Enable JavaScript and cookies to continue", '
        "sugira ao usuário carregar novamente o Oráculo!"
    )
    template = ChatPromptTemplate.from_messages([
        ('system', system_message),
        ('placeholder', '{chat_history}'),
        ('user', '{input}')
    ])
    chat = config_modelos['Groq']['chat'](model=modelo, api_key=api_key)
    chain = template | chat
    st.session_state['chain'] = chain

def pagina_chat():
    st.header('Bem-vindo ao Oráculo Acadêmico 🤖📚', divider=True)
    st.session_state.setdefault('memoria', ConversationBufferMemory())
    chain = st.session_state.get('chain')
    if chain is None:
        st.error('Carregue o Oráculo')
        st.stop()
    memoria = st.session_state['memoria']
    for mensagem in memoria.buffer_as_messages:
        st.chat_message(mensagem.type).markdown(mensagem.content)
    input_usuario = st.chat_input('Envie uma mensagem para o Oráculo')
    if input_usuario:
        st.chat_message('human').markdown(input_usuario)
        ai_message = st.chat_message('ai')
        resposta = ''
        for chunk in chain.stream({
            'input': input_usuario,
            'chat_history': memoria.buffer_as_messages
        }):
            resposta += chunk.content
        resposta_final = " ".join(resposta.split())
        ai_message.write(resposta_final)
        memoria.chat_memory.add_user_message(input_usuario)
        memoria.chat_memory.add_ai_message(resposta_final)

def sidebar():
    st.subheader('Configurações do Oráculo')
    caminho_diretorio = st.text_input('Diretório do Obsidian:', placeholder='/caminho/para/seu/diretório')
    modelo = st.selectbox('Modelo:', config_modelos['Groq']['modelos'])
    api_key = st.text_input('API Key da Groq:', value=st.session_state.get('api_key_Groq', ''), type='password')
    st.session_state['api_key_Groq'] = api_key
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Inicializar Oráculo'):
            if not caminho_diretorio.strip():
                st.error("Por favor, forneça o diretório.")
            elif not api_key.strip():
                st.error("Por favor, forneça a API key.")
            else:
                carrega_modelo(modelo, api_key, caminho_diretorio)
                st.session_state['memoria'] = ConversationBufferMemory()
    with col2:
        if st.button('Apagar Histórico'):
            st.session_state['memoria'] = ConversationBufferMemory()

def main():
    st.session_state.setdefault('memoria', ConversationBufferMemory())
    st.session_state.setdefault('chain', None)
    st.session_state.setdefault('api_key_Groq', '')
    with st.sidebar:
        sidebar()
    pagina_chat()

if __name__ == '__main__':
    main()