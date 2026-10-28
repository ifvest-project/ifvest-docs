# Registro de Versões

Este documento registra o histórico de evolução da plataforma IFVest, organizado por marcos de desenvolvimento. Cada versão corresponde a uma entrega relevante: nova funcionalidade, reestruturação técnica ou mudança significativa no banco de dados.

O IFVest nasceu de projetos de extensão do IFSP Campus Jacareí voltados à preparação para o ENEM e os vestibulares, coordenados desde 2018. A plataforma web surgiu em 2021, com a primeira versão registrada abaixo.

As versões anteriores ao IFVest V3 foram reconstituídas a partir dos TCCs e dos relatórios finais de iniciação científica, extensão e estágio guardados no acervo do projeto, e das migrations do banco de dados da versão 2. As fontes de cada versão estão no [fim desta página](#fontes-das-versoes-10-a-26).

!!! info "Versão atual: IFVest V3"
    A plataforma em produção é o **IFVest V3**, reconstruído do zero em 2026 e descrito na [última entrada](#v30-ifvest-v3-nova-plataforma-2026) desta página. As versões anteriores permanecem registradas como histórico.

---

## v1.0 — Plataforma PHP/MariaDB (2021)

**Período:** 2021  
**Responsáveis:** Rafael Rodrigues de Sousa (back-end e banco de dados), N. G. Fonseca (interface)  
**Tipo:** TCC

Primeira versão da plataforma IFVest, desenvolvida como trabalho de conclusão de curso, aprovado em dezembro de 2021. Implementada com PHP no back-end, MariaDB como banco de dados e o padrão MVC. O back-end e a interface foram desenvolvidos por pessoas diferentes e integrados ao longo do projeto.

**Funcionalidades entregues:**

- Cadastro com confirmação de e-mail, recuperação de senha e senhas criptografadas
- Perfis de aluno, professor e administrador
- Banco de questões de vestibular, com questões inseridas e classificadas pelos professores
- Simulados de até 10 questões, montados pelo aluno a partir da disciplina e dos tópicos
- Geração do simulado em PDF, para aplicação em sala de aula

**Observação:** não há registro de desenvolvimento da plataforma em 2022. O trabalho foi retomado em 2023, com a reescrita em Node.js.

---

## v2.0 — Reescrita em Node.js (2023–2024)

**Período:** 2023–2024  
**Responsável:** Cristian Rodolfo Zago Da Silva  
**Tipo:** TCC + Iniciação Científica (PIBIFSP 2024)

Reescrita completa da plataforma, abandonando PHP/MariaDB em favor de uma stack moderna. A nova arquitetura adota o padrão MVC. O trabalho foi apresentado no 14º Congresso de Inovação, Ciência e Tecnologia do IFSP (CONICT), em 2023, e entregue no início de 2024 a quem deu continuidade ao projeto.

No mesmo ano, Marcelo Corrêa desenvolveu um editor de equações matemáticas de código aberto para o projeto, apresentado no mesmo congresso e incorporado à plataforma a partir de 2024.

**Stack adotada:**

- Node.js + Express
- MySQL (Sequelize ORM)
- EJS (template engine)
- Bootstrap 5

**Funcionalidades entregues:**

- Autenticação com bcrypt e sessões
- Perfis de usuário: Aluno e Professor, com página de perfil
- Criação e gerenciamento de questões objetivas e dissertativas
- Módulo de simulados (criação, edição, realização e gabarito), com temporizador que envia o simulado quando o tempo acaba
- Videoaulas cadastradas por professores e administradores
- Geração de PDF de simulados

**Migrations do banco de dados:**

| Data | Tabela criada |
|---|---|
| 2023-03-19 | `Usuario` |

---

## v2.1 — Reestruturação, PostgreSQL e curadoria com IA (2024)

**Período:** 2024  
**Responsáveis:** Ruan Patrick Santos Araujo (reestruturação, banco de dados e editores); Guilherme Oliveira de Souza (curadoria com IA); Rafaela dos Santos Machado (testes)  
**Tipo:** Estágio supervisionado, Iniciação Científica e Extensão

Continuação da versão 2. As rotas, as páginas e o banco de dados foram reestruturados para atender ao objetivo central da plataforma — resolver simulados na própria plataforma ou impressos —, e o banco migrou do MySQL para o PostgreSQL. No mesmo período, foi integrada a primeira ferramenta de inteligência artificial da plataforma, para apontar questões semelhantes no banco.

**Funcionalidades entregues:**

- Banco de dados reestruturado: alternativas numa tabela própria, com a indicação da correta, e tópicos que o usuário cria e vincula às questões
- Migração do banco de dados do MySQL para o PostgreSQL
- Editor de texto (Quill) e editor de equações, adaptado do editor de Marcelo Corrêa, na criação de questões
- Verificação de questões semelhantes com a API Gemini (Google): ao cadastrar uma questão, o professor vê se já há outra parecida no banco, mesmo com outra redação
- Hospedagem em serviços de nuvem (Render e Infinite Cloud Computing)
- Testes de software e de acessibilidade ao longo do desenvolvimento

**Migrations do banco de dados:**

| Data | Tabela criada |
|---|---|
| 2024-03-19 | `Area`, `Topico` |
| 2024-03-20 | `Questao`, `Simulado`, `Opcao`, `Resposta`, `PerguntasProvas` |
| 2024-04-17 | `QuestaoTopico` (relação N:M entre questões e tópicos) |

---

## v2.2 — Editor Markdown e Módulo de Revisão de Conteúdo (2025)

**Período:** 2025  
**Responsáveis:** João Pedro Veríssimo Gonçalves (módulo de revisão e arquitetura de domínios); Ruan Patrick Santos Araujo (editor Markdown)  
**Tipo:** Iniciação Científica + Extensão

Introdução do módulo de revisão de conteúdo para professores criarem e alunos consumirem materiais de estudo em Markdown. Neste período também foi proposta e implementada a separação da aplicação em domínios isolados (`domains/`), que organizou a versão 2 até a sua substituição pelo IFVest V3.

**Funcionalidades entregues:**

- Editor Markdown com preview em tempo real (React + Vite, isolado em `editor_markdown/`)
- Suporte a notação matemática LaTeX via KaTeX, no lugar do MathJax usado antes
- Módulo de revisão: criação, edição e exclusão de materiais por professores
- Navegação hierárquica por assuntos (árvore de categorias)
- Busca de conteúdo por área, tópico e assunto
- Upload de arquivos para materiais
- Contador de leituras por conteúdo

**Migrations:**

| Data | Tabela criada |
|---|---|
| 2025-02-02 | `Assunto` (com suporte a hierarquia via `id_assunto_ascendente`) |
| 2025-03-26 | `Session` (persistência de sessões no banco) |
| 2025-05-19 | `PalavraChave`, `Conteudo`, `TagConteudo` |

---

## v2.3 — Módulo de Flashcards (2025)

**Período:** 2025  
**Responsável:** André Vinícius Neves da Silva  
**Tipo:** Extensão

Implementação do módulo de flashcards com lógica de repetição espaçada integrada à plataforma.

**Funcionalidades entregues:**

- CRUD de flashcards para professores (criar, editar, excluir)
- Interface de estudo para alunos com filtros por Área, Tópico e Dificuldade
- Exibição de até 10 cartões aleatórios por sessão
- Animação de virada de cartão para revelação da resposta
- Repetição espaçada baseada no campo `visto_por_ultimo` com intervalos de 1, 3, 7, 15 e mais de 15 dias
- Navegação por grupos de flashcards
- Três níveis de dificuldade: Fácil, Médio, Difícil

**Migrations:**

| Data | Tabela criada |
|---|---|
| 2025-01-01 | `Dificuldade` |
| 2025-01-01 | `Flashcard` |
| 2025-09-18 | `FlashcardUsuario` (rastreamento de revisões por usuário) |

---

## v2.4 — IFQuiz (2025)

**Período:** 2025  
**Responsável:** Nicolas Felipe Pinheiro Soares  
**Tipo:** Extensão

Adição do IFQuiz, módulo de quizzes com elementos de gamificação.

**Funcionalidades entregues:**

- Quizzes de múltipla escolha com questões do ENEM via API `enem.dev`
- Seleção de matéria e quantidade de questões
- Feedback imediato por questão (correto/incorreto)
- Tela de resultados com acertos e percentual de eficiência
- Ranking dos 5 melhores jogadores (placar público)
- Registro de pontuação para usuários logados e visitantes

**Migrations:**

| Data | Alteração |
|---|---|
| 2025-10-28 | Campo `descricao` do `Simulado` alterado de `STRING` para `TEXT` |
| 2025-11-15 | Tabela `Placar` criada |
| 2025-12-06 | Adição de `id_placar` (PK) à tabela `Placar` |
| 2025-12-06 | Renomeação da tabela de placar para nome definitivo |

---

## v2.5 — LGPD e Adequação Legal (2025)

**Período:** 2025  
**Responsável:** Kendy de Oliveira Outi  
**Tipo:** Extensão

Análise de conformidade com a Lei Geral de Proteção de Dados (LGPD) e implementação das soluções documentais e de interface exigidas.

**Funcionalidades entregues:**

- Mapeamento dos dados pessoais coletados pela plataforma
- Texto da Política de Privacidade elaborado com embasamento jurídico
- Página de Política de Privacidade integrada à plataforma em `/shared/politica_de_privacidade`
- Propostas de canais de atendimento ao titular de dados

---

## v2.6 — Acessibilidade (2025)

**Período:** 2025  
**Responsável:** Rafaela dos Santos Machado  
**Tipo:** Estágio supervisionado

Correções de acessibilidade na interface da versão 2, guiadas pelas diretrizes WCAG e priorizando, num primeiro momento, as pessoas com deficiência visual.

**Funcionalidades entregues:**

- Correções na estrutura semântica, nos rótulos, nos atributos ARIA e no controle de foco das páginas, começando pela de login
- Navegação por teclado e leitura com leitor de tela no módulo de Simulados — da criação à resolução, com os modais e a geração de PDF — e nos Flashcards e no IFQuiz
- Auditorias com as ferramentas WAVE, axe-core, Accessibility Insights for Web e Lighthouse, e verificação manual com o leitor de tela NVDA
- Teste do módulo de Simulados com um usuário cego, usando o NVDA

---

## v3.0 — IFVest V3: nova plataforma (2026)

**Período:** 2026  
**Responsáveis:** equipes do projeto de 2026, organizadas nos eixos de [Subprojetos Ativos](subprojetos/index.md)  
**Tipo:** Extensão + Programa Meninas nas Ciências

Reconstrução completa da plataforma, desenvolvida do zero e referida internamente como **IFVest V3**. Substituiu a versão anterior no mesmo endereço, com nova stack, novo modelo de dados e autorização por permissões granulares no lugar dos perfis fixos de aluno e professor.

A data de entrada no ar não está registrada no repositório. O registro datado mais antigo é a migration inicial, de **18/09/2026**. Como as tabelas já existiam, o banco de produção foi apenas marcado como estando nessa versão, em data que também não está registrada.

No código, a aplicação se identifica como versão **0.1.0**, numeração própria da nova base. Esta página mantém a sequência histórica e a registra como v3.0.

**Stack adotada:**

- React 19 e TypeScript, com Vite, no frontend
- Python 3.12 com FastAPI no backend
- PostgreSQL 16, com SQLAlchemy e Alembic
- Firebase Authentication, com login pela conta Google
- Docker Compose, num servidor próprio (VPS)

**Funcionalidades entregues:**

- Entrada com a conta Google, com criação da conta no primeiro acesso
- Permissões granulares, concedidas e revogadas por administradores
- IFQuiz com questões do banco próprio: quiz personalizado, Pergunta do Dia, sequência diária, patentes, ranking geral e semanal e loja de avatares
- Simulados de treino, visíveis só a quem os cria, e institucionais, visíveis a todos; manuais ou aleatórios, com resolução na plataforma, caderno e gabarito para impressão e registro das tentativas, com a resposta de cada questão
- Módulo de Redação: propostas com textos de apoio, envio de redações e correção pelas cinco competências do ENEM, com comentários em trechos do texto
- Banco de questões com cadastro, edição e denúncia de erros, e importação de provas em lote pelo painel administrativo, com simulação antes de gravar
- Painel administrativo com indicadores, gestão de permissões, moderação das denúncias e controle dos módulos por *feature flags*
- Registro de auditoria de cadastros e edições de questões, denúncias, propostas de redação, permissões e módulos, além das cargas e importações de questões

O detalhamento está na [Descrição das Funcionalidades](funcionalidades.md).

**Migrations do banco de dados:**

| Data | Alteração |
|---|---|
| 2026-09-18 | Schema inicial, registrado sobre o banco de produção existente, com 21 tabelas |
| 2026-09-18 | Tabela `feature_flags` |
| 2026-09-18 | Etiquetas nas propostas de redação e título nos textos de apoio |
| 2026-09-23 | Tabelas `question_reports` e `audit_logs` |
| 2026-09-26 | Datas sem fuso horário nas duas tabelas anteriores |
| 2026-09-27 | Divisão das permissões de conteúdo em quatro |
| 2026-09-27 | Remoção das duas permissões antigas |
| 2026-10-10 | Separação entre simulados institucionais e de treino |
| 2026-10-10 | Permissão `create_mocktest` renomeada para `create_institutional_mocktest` |
| 2026-10-10 | Tabela `user_mocktest_answers`, com a resposta de cada questão das tentativas de simulado |
| 2026-10-15 | Tabela `question_imports`, das importações de questões pelo painel |

**O que mudou em relação à versão anterior:**

| Versão 2 | IFVest V3 |
|---|---|
| Cadastro com nome de usuário, e-mail e senha | Entrada apenas com a conta Google |
| Perfis fixos de Aluno e Professor | Permissões granulares, sem perfis fixos |
| Questões objetivas e dissertativas | Apenas questões de múltipla escolha |
| Áreas de conhecimento e tópicos, com assuntos em árvore | Hierarquia Disciplina → Assunto → Tópico |
| IFQuiz com questões da API externa `enem.dev` e placar dos cinco melhores | IFQuiz com questões do banco próprio, pontos, patentes, ranking e loja |
| Flashcards e Revisão de Conteúdo em funcionamento | Previstos, ainda sem implementação |
| Verificação de questões semelhantes por IA (Gemini) | Não existe |
| Impressão de simulado por modelo próprio do servidor | Caderno de questões montado pelo navegador |
| Foto de perfil e exclusão de conta | Não existem |
| Página de Política de Privacidade | Não existe |
| — | Módulo de Redação, denúncias com moderação, registro de auditoria e *feature flags* |

---

## Próximos passos

Os módulos **Flashcards** e **Revisão de Conteúdo** estão previstos e já têm *feature flags*, desligadas por padrão, mas ainda não têm implementação. As frentes de trabalho em andamento estão em [Subprojetos Ativos](subprojetos/index.md).

---

## Fontes da versão 3.0

| Conteúdo | Fonte | Data |
|---|---|---|
| Stack e versão declarada no código | `ifvest-backend/pyproject.toml`, `ifvest-frontend/package.json` e configuração de produção do `ifvest-monorepo` | out/2026 |
| Funcionalidades | Código do backend e do frontend do `ifvest-monorepo`, até o commit `d36de12`, de 15/10/2026 | out/2026 |
| Migrations e adoção do Alembic | `ifvest-backend/alembic/versions/` e `deploy/README.md` | out/2026 |
| Comparação com a versão anterior | Versão 2 desta documentação, preservada na etiqueta `legado-v2` | out/2026 |
| Responsáveis e tipo | Lista dos projetos vinculados ao IFVest em 2026 e atas das reuniões dos grupos de trabalho | 2026 |

## Fontes das versões 1.0 a 2.6

| Versão | Fonte | Data |
|---|---|---|
| Origem | Súmula curricular da coordenação do projeto | 2026 |
| v1.0 | TCC de Rafael Rodrigues de Sousa, aprovado em 14/12/2021, e artigo de N. G. Fonseca sobre a interface, no 12º CONICT | 2021 |
| v2.0 | Relatório de iniciação científica de Cristian Rodolfo Zago Da Silva (PIBIFSP 2024, validado como TCC) e artigo de Marcelo Corrêa sobre o editor de equações, no 14º CONICT | 2023–2024 |
| v2.1 | Relatório de estágio supervisionado de Ruan Patrick Santos Araujo, relatório final de Guilherme Oliveira de Souza e relatório final de extensão de Rafaela dos Santos Machado | dez/2024 |
| v2.2 | Relatórios finais de João Pedro Veríssimo Gonçalves e de Ruan Patrick Santos Araujo | 2025 |
| v2.3 | Relatório final de extensão de André Vinícius Neves da Silva | nov/2025 |
| v2.4 | Relatório final de Nicolas Felipe Pinheiro Soares | nov/2025 |
| v2.5 | Relatório final de extensão de Kendy de Oliveira Outi | dez/2025 |
| v2.6 | Relatório de estágio supervisionado de Rafaela dos Santos Machado | dez/2025 |
| Migrations | Código da versão 2, conforme a versão anterior desta documentação (etiqueta `legado-v2`) | — |
