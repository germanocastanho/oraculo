# **Oráculo Acadêmico** 🤖📚

## 1. Introdução 📖

### 1.1 Contexto e Motivação

O **Oráculo Acadêmico** é um chatbot desenvolvido para auxiliar pesquisadores e estudantes que utilizam o Obsidian como ferramenta de organização acadêmica. Sua finalidade é tornar a interação com arquivos Markdown mais dinâmica e intuitiva, proporcionando acesso rápido a notas, textos e referências. Com isso, objetiva-se aprimorar a eficiência da pesquisa, automatizando a localização de informações relevantes.

### 1.2 Objetivos do Projeto

O projeto visa simplificar a navegação em grandes volumes de conteúdo textual, fornecendo respostas contextuais e resumidas com base nos arquivos armazenados. Dessa forma, o pesquisador pode focar na produção intelectual, delegando ao Oráculo o trabalho de recuperação de informações relevantes.

---

## 2. Arquitetura do Projeto 🛠️

### 2.1 Tecnologias Utilizadas

- **Streamlit**: Criação de interface web simples e interativa;
- **LangChain**: Fluxo conversacional e gerenciamento de memória do chatbot;
- **Modelos de Linguagem (LLMs)**: Suporte a diversos modelos, como `llama-3.1`, `gemma2` e `mixtral`;
- **Python 3.8+**: Linguagem principal do projeto.

### 2.2 Fluxo de Processamento

1. O usuário informa o diretório do seu cofre Obsidian, onde estão armazenados os arquivos Markdown.
2. O Oráculo processa os arquivos, extraindo e limpando o conteúdo textual, removendo formatações desnecessárias.
3. O conteúdo é otimizado, preservando apenas informações essenciais.
4. Com base nessas informações, o chatbot responde ao usuário, oferecendo respostas contextuais e mantendo um histórico da conversa.

---

## 3. Instalação e Configuração ⚙️

### 3.1 Pré-requisitos do Sistema

- **Python 3.8 ou superior** instalado;
- **Git** para clonar o repositório;
- **Conta na Groq** com API Key válida.

### 3.2 Instalação das Dependências

**Clonar Repositório**
```bash
git clone https://github.com/germanocastanho/oraculo.git
cd oraculo
```

**Criar Ambiente Virtual**
```bash
python3 -m venv .venv
```

**Ativar Ambiente Virtual**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

**Instalar Pacotes Necessários**
```bash
pip install -r requirements.txt
```

### 3.3 Obtenção e Uso da API Key

Obtenha sua API Key junto à Groq. Em seguida, ao iniciar a aplicação, insira a chave no campo apropriado para ativar o modelo de linguagem desejado.

### 3.4 Preparação do Cofre Obsidian

Antes de iniciar, certifique-se de que seus arquivos Markdown estejam organizados e acessíveis. Forneça o caminho correto ao Oráculo para garantir o processamento adequado do conteúdo.

### 3.5 Inicialização da Aplicação

```bash
streamlit run oraculo.py
```

---

## 4. Uso da Interface 🖥️

### 4.1 Navegação Básica

A interface possui uma barra lateral para configurações, onde você pode definir o diretório do cofre, o modelo de linguagem e a chave de API. Na área central, interaja com o chatbot enviando suas perguntas.

### 4.2 Ajustes de Modelo e Memória

Escolha o modelo de linguagem mais adequado à sua necessidade. É possível redefinir o histórico de conversa a qualquer momento, iniciando um novo diálogo sem influências do anterior.

### 4.3 Interação via Chat

O Oráculo responde às perguntas com base nos arquivos disponíveis. Em caso de erro ou respostas inconsistentes, como mensagens genéricas (“Just a moment…Enable JavaScript and cookies to continue”), siga as instruções para recarregar o sistema.

---

## 5. Melhores Práticas 🌟

### 5.1 Organização dos Arquivos Markdown

Para obter os melhores resultados, mantenha seus arquivos Markdown bem estruturados. Agrupe temas de forma coerente, utilize títulos e seções claras, e evite duplicatas ou conteúdo irrelevante.

### 5.2 Limitações de Contexto e Solução de Problemas

Caso o Oráculo não encontre a informação desejada, tente reformular sua pergunta ou ampliar o contexto. Certifique-se também de que o conteúdo necessário esteja acessível e legível.

---

## 6. Licença e Contribuições 📜

### 6.1 Licenciamento (GPL-3.0)

Este projeto é licenciado sob a [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.html), garantindo sua natureza livre e aberta para uso e distribuição.

### 6.2 Como Contribuir

Feedbacks, sugestões de melhoria e contribuições de código são bem-vindos! Basta abrir issues ou enviar pull requests no repositório.

---

## 7. Contato e Suporte ✉️

Em caso de dúvidas ou problemas, abra uma issue no repositório ou entre em contato pelo e-mail [germanocastanho@proton.me](mailto:germanocastanho@proton.me). O suporte será fornecido sempre que possível!