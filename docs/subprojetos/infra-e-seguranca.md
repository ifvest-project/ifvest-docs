# Eixo 4: Infraestrutura, APIs e Segurança

Este eixo garante a robustez, a segurança e a conformidade legal da infraestrutura da plataforma IFVest. Os projetos visam desenvolver APIs para integração com serviços externos, aprimorar a gestão de dados e assegurar a proteção das informações dos usuários.

## Projetos Principais

### Adequação do Cadastro da IFVest à LGPD

*   **Líder:** Wilker
*   **Objetivo:** Garantir a conformidade do sistema de cadastro do IFVest com a Lei Geral de Proteção de Dados (LGPD), Lei n.º 13.709/2018.
*   **Tecnologias Envolvidas:** Firebase (Firebase Authentication, Cloud Firestore, Cloud Storage).
*   **Destaques:**
    *   Reestruturação técnica do banco de dados do cadastro com Firebase, utilizando Firebase Authentication para autenticação segura com hash de senhas via bcrypt.
    *   Configuração do Cloud Firestore com Security Rules para isolamento de dados por usuário.
    *   Configuração do Cloud Storage para armazenamento seguro de fotos de perfil.
    *   Formalização das bases legais para cada dado coletado, conforme exigido pelo art. 7.º da LGPD.
    *   Adoção de uma arquitetura integralmente aderente aos princípios de Segurança, Necessidade e Finalidade da LGPD.

### Criação de Tags para Integração com API do ENEM e Estruturação do Banco de Dados das Questões

*   **Líder:** Victor
*   **Objetivo:** Criar tags para a integração com a API do ENEM e estruturar o banco de dados das questões, para suportar a categorização e a busca.
*   **Destaques:**
    *   Criação de um sistema de tags robusto para classificar questões por disciplina, tópico e subtópico.
    *   Estudo e integração com APIs externas (como `enem.dev`) para importação automatizada de questões.
    *   Definição do contrato de dados em JSON com as equipes de extração de provas e escolha do PostgreSQL para o banco de questões.
    *   Modelagem de dados para um banco de questões escalável e de fácil manutenção.
    *   Apoio à criação de simulados personalizados e materiais de revisão.

### API para Extração de Questões da Unicamp

*   **Líder:** Henrique Mosson Zaianz
*   **Objetivo:** Extrair as questões das provas da Unicamp, em PDF, e estruturá-las em JSON para alimentar o banco de questões.
*   **Tecnologias Envolvidas:** Python, PyMuPDF e OCR (para a leitura das provas) e Pydantic (para o esquema dos dados).
*   **Destaques:**
    *   Definição do formato e da tipagem dos dados extraídos, documentados com Pydantic e num README.
    *   Extração do texto e das figuras das provas, com validação do conjunto de dados extraído.
    *   Testes da extração com provas da FUVEST.
    *   Estrutura do JSON repassada à extração de outros vestibulares.

### API para Extração de Questões de Outros Vestibulares

*   **Líder:** Thales
*   **Objetivo:** Estender a extração de questões a outros vestibulares, como a FUVEST, no mesmo formato de dados.
*   **Tecnologias Envolvidas:** Python e OCR.
*   **Destaques:**
    *   Início da extração dos dados das provas, com as provas reunidas num diretório de dados brutos.
    *   Levantamento de algoritmos de OCR e testes com bibliotecas de extração em Python.
    *   Tratamento das alternativas em imagem, em andamento.

### Reestruturação da Plataforma

*   **Líder:** Jorge
*   **Objetivo:** Coordenar a refatoração que deu origem ao IFVest V3, com o backend e o banco de dados reescritos em Python.
*   **Tecnologias Envolvidas:** Python, FastAPI, Docker e ferramentas de gerenciamento de projetos (Trello).
*   **Destaques:**
    *   Definição, com as equipes, do Python com FastAPI como padrão do backend.
    *   Reescrita de componentes do backend e do banco de dados em Python.
    *   Infraestrutura inicial de integração contínua, com Docker e verificações de qualidade.
    *   Organização das tarefas de desenvolvimento e migração utilizando ferramentas de gerenciamento de projetos como Trello.
