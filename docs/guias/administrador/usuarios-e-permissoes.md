# Usuários e Permissões

No IFVest V3, o que cada conta pode fazer depende das **permissões** que ela tem, e não de um perfil escolhido no cadastro. Na aba **Usuários e Permissões**, o administrador encontra as contas e concede ou revoga cada permissão.

O catálogo tem oito permissões:

| Permissão | O que permite | Como se obtém |
|---|---|---|
| `admin_permission` | Usar o Painel Administrativo. Passa em todas as verificações de permissão da plataforma | Automática só para o administrador inicial |
| `create_question` | Cadastrar questões no banco | Automática para e-mails `@ifsp.edu.br` |
| `edit_question` | Editar questões existentes e ver o gabarito no banco de questões | Automática para e-mails `@ifsp.edu.br` |
| `create_institutional_mocktest` | Criar simulados institucionais, que aparecem para todos | Automática para e-mails `@ifsp.edu.br` |
| `manage_mocktests` | Editar e excluir simulados criados por outras pessoas | Automática para e-mails `@ifsp.edu.br` |
| `create_essay_proposal_permission` | Criar, editar e excluir propostas de redação | Concedida por um administrador |
| `grade_essay_permission` | Corrigir redações | Concedida por um administrador |
| `audit_question` | Aprovar as questões pendentes na [Auditoria de Questões](auditoria-de-questoes.md) e editá-las antes da aprovação. Dá acesso ao Painel Administrativo, só com essa aba | Concedida por um administrador |

As permissões automáticas são atribuídas só no **primeiro acesso** da conta. Depois disso, valem as concessões e revogações feitas no painel: uma permissão revogada não volta sozinha.

---

## Tarefa 1 — Encontrar um usuário

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** localizar uma conta para conferir os seus dados e permissões.

**Pré-requisitos:** a pessoa ter entrado na plataforma ao menos uma vez — a conta é criada no primeiro acesso.

**Como fazer:**

1. No Painel Administrativo, abra a aba **Usuários e Permissões**.
2. Busque em **Pesquisar usuário por email, apelido ou permissão...**. A lista vem em páginas de 20 usuários.
3. Cada usuário mostra o apelido — ou **Sem apelido** —, o e-mail, os pontos e a sequência diária do IFQuiz e, em **Permissões**, as permissões que tem, ou **Nenhuma permissão especial**.

**Observações:**

- Para listar quem tem uma permissão, busque pelo nome dela — por exemplo, `grade_essay_permission`.
- Não há como cadastrar uma conta pelo painel: quem ainda não entrou na plataforma não aparece na lista.

---

## Tarefa 2 — Conceder uma permissão

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** dar a uma conta a autorização para uma tarefa, como corrigir redações.

**Pré-requisitos:** ter encontrado o usuário ([Tarefa 1](#tarefa-1-encontrar-um-usuario)).

**Como fazer:**

1. No cartão do usuário, abra a lista **+ Conceder nova permissão...** e escolha a permissão. Cada opção traz o nome e a descrição.
2. Clique em **Conceder**. A mensagem *"Permissão "…" concedida com sucesso!"* confirma, e a permissão aparece no cartão.

**Observações:**

- A lista oferece só as permissões que a conta ainda não tem. Com todas concedidas, o cartão mostra *"Todas as permissões do sistema já atribuídas."*
- A permissão vale na hora para as ações. Já as abas e os botões que ela libera, como a aba **Professor** ou, com `audit_question`, a aba **Admin**, aparecem para a pessoa quando ela recarrega a página ou entra de novo.
- Conceda a permissão de administrador só a quem vai administrar a plataforma: ela libera todas as outras. Para quem só vai aprovar questões, basta a `audit_question`.

---

## Tarefa 3 — Revogar uma permissão

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** tirar de uma conta uma autorização que ela não deve mais ter.

**Pré-requisitos:** ter encontrado o usuário ([Tarefa 1](#tarefa-1-encontrar-um-usuario)).

**Como fazer:**

1. No cartão do usuário, em **Permissões**, clique no **×** da permissão.
2. A mensagem *"Permissão "…" removida com sucesso!"* confirma, e a permissão some do cartão.

!!! warning "A revogação não pede confirmação"
    A permissão é retirada no primeiro clique no **×**. Se você revogar a permissão errada, conceda-a de novo pela [Tarefa 2](#tarefa-2-conceder-uma-permissao).

    Revogar a sua própria `admin_permission` tira o seu acesso ao painel. Para recuperá-lo, outro administrador precisa concedê-la de novo.

**Observações:**

- A permissão de administrador do administrador inicial não pode ser revogada: a tentativa termina em *"Erro ao remover permissão."*
- Revogar uma permissão não desfaz o que a pessoa fez com ela. As questões cadastradas, as propostas publicadas e as correções enviadas continuam na plataforma.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| Não encontro a pessoa na lista | Ela ainda não entrou na plataforma, ou usou outro e-mail. Peça que entre com a conta Google e busque de novo |
| *"Erro ao conceder permissão."* | Recarregue a página e tente de novo |
| *"Erro ao remover permissão."* | Se a permissão é a `admin_permission` do administrador inicial, ela não pode ser revogada. Nos demais casos, recarregue a página e tente de novo |
| A pessoa recebeu a permissão, mas não vê a tela | Peça que recarregue a página ou saia e entre de novo |
| *"Não foi possível carregar o catálogo de permissões. Tente novamente mais tarde."* | A lista de permissões para conceder não carregou. Recarregue a página |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tela, ações e mensagens | Código do frontend do `ifvest-monorepo` (commit `f98a6a0`): Painel Administrativo, aba Usuários e Permissões | nov/2026 |
| Catálogo de permissões e regras de concessão e revogação | `ifvest-backend/src/core/permission_catalog.py`, `src/core/permissions.py` e `src/api/v1/users.py`, no `ifvest-monorepo` | nov/2026 |
| Permissões automáticas | [Descrição do Sistema — Como as permissões são atribuídas](../../descricao-do-sistema.md#como-as-permissoes-sao-atribuidas) | out/2026 |
