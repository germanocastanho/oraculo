# **Oráculo Acadêmico** 🤖📚

Projetado para pesquisadores, estudantes e entusiastas, o **Oráculo** é uma ferramenta poderosa e intuitiva que transforma documentos Markdown em conhecimento acionável. Com tecnologias avançadas de inteligência artificial generativa, ele processa, resume e recupera informações relevantes com rapidez e precisão. Totalmente compatível com ferramentas como o [Obsidian](https://obsidian.md/), o Oráculo proporciona uma experiência fluida, transformando diretórios de arquivos `.md` em cofres de conhecimento acessível, enquanto você explora suas ideias. ✨

## 🛠️ Funcionalidades Principais

- **Automação Inteligente** 🚀: Analise e resuma documentos Markdown com eficiência, otimizando tarefas repetitivas para poupar tempo e esforço.
- **Busca Avançada** 🔍: Recupere informações relevantes em segundos, utilizando índices vetoriais e modelos de linguagem de última geração.
- **Personalização Flexível** 🛠️: Configure o modelo de IA, insira sua chave API e escolha o diretório de trabalho conforme suas necessidades.
- **Conversa Inteligente** 💬: Receba respostas detalhadas e contextuais baseadas no conteúdo de seus arquivos, com suporte a histórico de interação.
- **Fácil Integração** 🤝: Totalmente compatível com ferramentas como o [Obsidian](https://obsidian.md/), permitindo o uso direto de diretórios sem configurações complexas.
- **Interface Amigável** 🎨: Design acessível e responsivo em [Streamlit](https://streamlit.io/), pensado para todos os tipos de usuários.

## 📋 Pré-requisitos e Instalação

### **Pré-requisitos**

Antes de começar, certifique-se de ter:
- [**Python 3.8+**](https://www.python.org/) 🐍: Versão mínima recomendada para compatibilidade com as dependências do projeto.  
- **Chave API** 🔑: Necessária para acessar os modelos de GenAI, como ChatGPT-4o ([OpenAI](https://openai.com/)) ou Llama 3.3 ([Groq](https://groq.com/)).
- **Bibliotecas** 📚: Dependências listadas no arquivo [`requirements.txt`](requirements.txt), que incluem ferramentas [LangChain](https://www.langchain.com/) e [FAISS](https://faiss.ai/).

### **Instalação**

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/germanocastanho/oraculo.git
   ```
2. **Navegue até o diretório**:
   ```bash
   cd oraculo
   ```
3. **(Opcional) Crie um VENV**:

- Linux/macOS:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   
- Windows:
   ```cmd
   python -m venv .venv
   .venv\Scripts\activate
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute o Oráculo**:
   ```bash
   streamlit run oraculo.py
   ```

## 🚀 Configuração e Utilização

### **Configurar suas Preferências**

- Escolha o modelo de IA ([ChatGPT-4o](https://openai.com/index/hello-gpt-4o/) ou [Llama 3.3](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/)) e insira a chave API ([OpenAI](https://openai.com/) ou [Groq](https://groq.com/), respectivamente).
- Forneça o diretório contendo seus arquivos `.md`, seja do [Obsidian](https://obsidian.md/), seja de outro software compatível.

### **Utilizar o Oráculo**

- Utilize a interface de chat para enviar perguntas relacionadas ao conteúdo dos seus documentos.
- Obtenha resumos e insights, economizando tempo com a análise automatizada de grandes volumes de texto.

### **Exemplo Prático de Uso**

Veja como o Oráculo transforma sua pesquisa acadêmica com um exemplo. Imagine que você possui um diretório com anotações acadêmicas sobre filosofia política ou qualquer outro tema. Basta carregar esse diretório, e o Oráculo estará pronto para responder questões como:

- "Quais são as principais ideias de Rousseau sobre o contrato social?"
- "Resuma as diferenças entre Hobbes e Locke em relação ao estado de natureza."
- "Quais são os principais argumentos críticos ao capitalismo em Marx?"

## 🗂️ Arquitetura do Projeto

```
oraculo/
|-- interface/           # Módulos da interface do usuário
|-- logica/              # Lógica principal e modelos de IA
|-- config.json          # Configurações do usuário
|-- LICENSE              # Arquivo de licença (GPL-3.0)
|-- README.md            # Documentação do projeto
|-- requirements.txt     # Dependências do Python
|-- oraculo.py           # Script para iniciar a aplicação
```

## ⚙️ Detalhes Técnicos

1. **Modelos de GenAI**: Suporte nativo para [ChatGPT-4o](https://openai.com/index/hello-gpt-4o/) e [Llama 3.3](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/), com uma arquitetura flexível que facilita a incorporação de novos modelos, garantindo adaptabilidade para diferentes contextos de uso.
2. **Sumarização e Indexação**: Utiliza pipelines avançados com [LangChain](https://www.langchain.com/) para processamento de texto, [FAISS](https://faiss.ai/) para buscas vetoriais otimizadas e embeddings da [HuggingFace](https://huggingface.co/blog/getting-started-with-embeddings) para representação semântica precisa.
3. **Memória Conversacional**: Armazena o histórico de interações, permitindo respostas mais precisas e alinhadas ao contexto da conversa.
4. **Interface e Configuração**: Desenvolvida com o [Streamlit](https://streamlit.io/), a interface é intuitiva e responsiva. As preferências do usuário são armazenadas em JSON, garantindo continuidade entre sessões e facilidade de personalização.

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Se deseja colaborar, siga boas práticas de programação e implemente melhorias. Faça um fork do repositório e implemente suas alterações. Envie um pull request com uma descrição clara do que foi feito. Caso encontre problemas ou tenha ideias, abra uma [issue](https://github.com/germanocastanho/oraculo/issues). Juntos, podemos tornar o Oráculo ainda mais incrível! 🚀

## 📜 Licença GPL-3.0

Distribuído sob a [Licença Pública Geral GNU v3.0 (GPL-3.0)](https://www.gnu.org/licenses/gpl-3.0.html), garantindo liberdade de uso, modificação e redistribuição do software, desde que os mesmos direitos sejam preservados em quaisquer versões derivadas. Ao utilizar ou contribuir com o projeto, você apoia a filosofia de software livre e a promoção de um ambiente colaborativo e aberto para inovação. 🔬

## ✉️ Contato e Créditos

- **Créditos**: Copyleft 🄯, Germano Castanho, 2024
- **E-mail**: [germanocastanho@proton.me](mailto:germanocastanho@proton.me)
- **Problemas?**: Abra uma [issue](https://github.com/germanocastanho/oraculo/issues) no repositório oficial

---

### **Cada linha, um manifesto pela liberdade!** ✊🏴