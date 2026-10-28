# Guia do Professor

Este guia documenta as tarefas de **criação e gestão de conteúdo** do IFVest: o banco de questões, os simulados institucionais e a importação de provas.

!!! info "Este guia complementa o Guia do Aluno"
    Quem tem as permissões de professor usa a plataforma como qualquer estudante, com tarefas a mais. Este guia cobre apenas o que se soma:

    - **Conta e perfil** — entrar, sair e consultar o perfil ficam na [seção Conta](../conta/acesso.md), comum a todos.
    - **Tarefas de estudo** — jogar o IFQuiz e montar e resolver simulados funcionam para você como para o estudante, e estão no [Guia do Aluno](../aluno/index.md).

!!! info "Versão documentada"
    O guia descreve o **IFVest V3**, em produção, conferido no código em outubro de 2026. As páginas de **Flashcards** e **Materiais de Revisão** registram módulos que ainda não foram implementados, com um aviso no início. Ver [Qual versão da plataforma estes guias descrevem](../index.md#qual-versao-da-plataforma-estes-guias-descrevem).

---

## Para quem é este guia

Professores e educadores que produzem e mantêm o conteúdo do IFVest. Nenhum conhecimento técnico de programação é necessário.

**Permissões:** no IFVest V3 não há perfis fixos de aluno e professor. O que você pode fazer depende das **permissões** da sua conta:

| Permissão | O que permite | Como se obtém |
|---|---|---|
| `create_question` | Cadastrar questões no banco | Automática para e-mails `@ifsp.edu.br` |
| `edit_question` | Editar questões existentes. A tela de edição fica no Painel Administrativo (ver [Editar uma questão](banco-de-questoes.md#tarefa-3-editar-uma-questao)) | Automática para e-mails `@ifsp.edu.br` |
| `create_institutional_mocktest` | Criar simulados institucionais, que aparecem para todos | Automática para e-mails `@ifsp.edu.br` |
| `manage_mocktests` | Renomear e excluir simulados criados por outras pessoas | Automática para e-mails `@ifsp.edu.br` |
| `create_essay_proposal_permission` | Publicar propostas de redação | Concedida por um administrador |
| `grade_essay_permission` | Corrigir redações | Concedida por um administrador |
| `admin_permission` | Administrar a plataforma, inclusive a moderação e a importação de questões | Concedida por um administrador |

As permissões automáticas são atribuídas no **primeiro acesso**. Se você entrou com outro e-mail, ou precisa de uma permissão que não tem, peça-a a um administrador. As suas permissões ativas aparecem no seu [perfil](../conta/perfil.md#tarefa-1-consultar-o-seu-perfil).

---

## Mapa das áreas de gestão

| Área | Onde fica | O que você faz nela | Situação |
|---|---|---|---|
| **Banco de questões** | Área do Professor (aba **Professor**) | Consultar e cadastrar questões | ✅ Disponível |
| **Simulados institucionais** | Simulados → **Criar novo simulado** | Criar simulados para todos os estudantes e gerenciar os de outras pessoas | ✅ Disponível |
| **Moderação de questões** | Painel Administrativo (aba **Admin**) | Editar questões e tratar as denúncias de erro | ✅ Disponível, só para administradores |
| **Importação de questões** | Painel Administrativo (aba **Admin**) | Importar provas em lote, a partir de um arquivo `.zip` | ✅ Disponível, só para administradores |
| **Propostas e correção de redações** | Área do Professor e Redação | Publicar propostas e corrigir redações | ✅ Disponível — ⬜ guia pendente |
| **Flashcards** | — | Criar os cartões de estudo | 🔵 Previsto |
| **Materiais de revisão** | — | Escrever os materiais de cada tópico | 🔵 Previsto |

A **Área do Professor** (`/area_professor`) aparece como a aba **Professor** do cabeçalho para quem tem qualquer uma das permissões de conteúdo ou de redação. Ela reúne três abas: **Banco de Questões**, **Propostas de Redação** e **Fila de Correção**.

Não há uma tela para organizar disciplinas, assuntos e tópicos: eles são criados ao [cadastrar uma questão](banco-de-questoes.md#tarefa-2-cadastrar-uma-questao).

Os termos usados na plataforma estão explicados no [Glossário](../glossario.md).

---

## Como ler as tarefas deste guia

Cada tarefa segue a estrutura explicada em [Como ler as tarefas](../index.md#como-ler-as-tarefas). O campo **Acesso** indica a permissão exigida — ele substitui o antigo campo **Perfil**, criado quando a divisão de tarefas entre professor e administrador ainda estava em discussão.

---

## Estrutura do guia

As páginas estão na ordem sugerida de leitura: primeiro o banco de questões, que alimenta os simulados; depois os demais tipos de conteúdo.

| Página | Conteúdo | Situação |
|---|---|---|
| [Acesso e Conta](../conta/acesso.md) | Entrar com a conta Google e sair | ✅ Comum a todos |
| [Perfil e Seus Dados](../conta/perfil.md) | Apelido, indicadores e históricos | ✅ Comum a todos |
| [Banco de Questões](banco-de-questoes.md) | Consultar, cadastrar, editar e importar questões; tratar as denúncias | ✅ Disponível |
| [Simulados](simulados.md) | Criar simulados institucionais e gerenciar simulados | ✅ Disponível |
| [Flashcards](flashcards.md) | Registro do módulo planejado | 🔵 Módulo previsto |
| [Materiais de Revisão](materiais-de-revisao.md) | Registro do módulo planejado | 🔵 Módulo previsto |

---

## Conformidade com as normas

Este guia integra, junto com o [Guia do Aluno](../aluno/index.md) e a [seção Conta](../conta/acesso.md), o item **"Documentação de Usuário"** previsto no mapeamento da **ISO/IEC/IEEE 15289:2019** adotado pelo projeto (ver [Planejamento da Documentação](../../planejamento.md)), com estrutura e conteúdo conforme a **ISO/IEC/IEEE 26514:2022**. Ambas as normas permitem **adaptação ao contexto do projeto** (*tailoring*), desde que a seleção de elementos aplicados e adiados seja registrada. Este é o registro:

| Elemento da 26514 | Onde está | Situação |
|---|---|---|
| Análise de público-alvo e tarefas | Seção "Para quem é" + inventário de tarefas por área | ✅ Aplicado |
| Informação instrucional (tarefas passo a passo) | Corpo das páginas | 🟡 Banco de questões e simulados revisados para o V3; propostas e correção de redações pendentes |
| Informação conceitual | "Mapa das áreas de gestão" + introdução de cada página | ✅ Aplicado |
| Solução de problemas | Seção "Erros e situações comuns" de cada página | ✅ Aplicado |
| Mensagens de erro (textos exatos) | Nas tabelas de erros, conferidas no código | 🟡 Aplicado onde há mensagem definida |
| Informação de referência | Coberta fora do guia pela [Descrição das Funcionalidades](../../funcionalidades.md) | ✅ Coberto pela Fase 3 |
| Glossário | [Glossário](../glossario.md), comum aos guias | ✅ Aplicado |
| Acessibilidade | [Seção comum aos guias](../index.md#acessibilidade-da-plataforma) | 🟡 Normas de referência identificadas e convenções definidas; a interface do V3 ainda não foi avaliada |
| Atribuição de permissões | Campo **Acesso** em cada tarefa + tabela de permissões | ✅ Aplicado |
| Validação com usuários | Prevista conforme a **ISO/IEC/IEEE 26513** | ⬜ Pendente — possível agora que a interface foi entregue |
