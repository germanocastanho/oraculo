# Oráculo Acadêmico 🤖

### Descrição:

O **Oráculo Acadêmico** é um chatbot projetado para interagir com arquivos markdown armazenados em cofres do Obsidian. Seu principal objetivo é facilitar a **busca, navegação e gestão de conteúdos acadêmicos**, atendendo especialmente pesquisadores que utilizam o Obsidian como ferramenta para organização e redação. O projeto prioriza **acessibilidade**, **modularidade** e **escalabilidade**, tornando-se adaptável a diferentes contextos acadêmicos e de pesquisa.

### Características Principais:

- **Processamento Avançado de Markdown**: Extração e limpeza de texto para garantir respostas precisas e relevantes.  
- **Integração Direta com Obsidian**: Compatível com cofres complexos e grandes volumes de dados.  
- **Respostas Estruturadas**: Otimização para recuperação de informações acadêmicas e elaboração de insights.
- **Configurações personalizáveis**: Permite configurar modelos e limites de processamento de acordo com as necessidades do usuário.
- **Interface Intuitiva**: Desenvolvida em Streamlit, promove uma experiência interativa e simplificada.
- **Público-Alvo**: Pesquisadores e estudantes que buscam aprimorar a organização e recuperação de conteúdos no ambiente do Obsidian.

### Detalhes Técnicos:

- **Base Tecnológica**: Utilização do LangChain para fluxo conversacional e memória.
- **Modelos Avançados**: Compatibilidade com LLMs como `llama-3.1`, `gemma2`, e `mixtral`.
- **Estratégias de Sumarização**: Textos grandes são resumidos para facilitar a manipulação.
- **Histórico de Conversas**: Implementação de `ConversationBufferMemory` para gestão de diálogos contínuos.

### Contribuição:

Este projeto está aberto à contribuição da comunidade.
Sugestões, melhorias e colaborações são altamente encorajadas para expandir sua funcionalidade e utilidade.

### Instalação

**1. Pré-requisitos**

Certifique-se de que os seguintes itens estão instalados no seu sistema:

- **Python 3.8 ou superior**: Baixe e instale a versão mais recente em [python.org](https://www.python.org/).
- **Git**: Necessário para clonar o repositório. Baixe em [git-scm.com](https://git-scm.com/).
- **Conta Groq**: Obtenha uma API Key válida em sua conta Groq para utilizar os modelos compatíveis.

---

**2. Clonar Repositório**

No terminal, execute os comandos abaixo para clonar o repositório do projeto e acessar o diretório clonado:

```bash
git clone https://github.com/germanocastanho/oraculo.git
cd oraculo
```

---

**3. Criar e Ativar Ambiente Virtual**

Configure um ambiente virtual para isolar as dependências do projeto:

1. Crie o ambiente virtual:
    
    ```bash
    python -m venv venv
    ```
    
2. Ative o ambiente virtual:
    
    - **Windows**:
        
        ```bash
        venv\Scripts\activate
        ```
        
    - **macOS/Linux**:
        
        ```bash
        source venv/bin/activate
        ```

---

**4. Instalar Dependências**

Instale todas as bibliotecas necessárias executando:

```bash
pip install -r requirements.txt
```

---

**5. Executar Chatbot**

Inicie o chatbot com o seguinte comando:

```bash
streamlit run oraculo.py
```

A aplicação será aberta automaticamente no navegador. Caso isso não ocorra, copie e cole o endereço exibido no terminal em seu navegador.

---

Pronto! O Oráculo Acadêmico está configurado e pronto para uso. 🚀
