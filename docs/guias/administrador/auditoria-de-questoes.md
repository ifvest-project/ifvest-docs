# Auditoria de Questões

Toda questão nova entra no banco **pendente de auditoria**. Isso vale para as questões cadastradas pelos professores no banco de questões e para as trazidas pela [importação](importacao-de-questoes.md) ou pela carga feita no servidor. Uma questão pendente não aparece no IFQuiz, na Pergunta do Dia nem nos simulados. Na aba **Auditoria de Questões** do Painel Administrativo, quem tem a permissão de auditoria confere cada questão, corrige o que for preciso e a aprova. A partir daí, ela passa a ser usada na plataforma.

No banco de questões da Área do Professor, quem cadastra ou edita questões vê as pendentes com o selo **Pendente de Auditoria** (ver [Guia do Professor — Banco de Questões](../professor/banco-de-questoes.md)).

!!! info "Auditoria de questões não é o registro de auditoria"
    A **auditoria de questões**, desta página, é a aprovação das questões antes de entrarem em uso. O **registro de auditoria** é o histórico das alterações feitas na plataforma, apresentado em [Indicadores e Auditoria](indicadores-e-auditoria.md). Cada aprovação também fica nesse registro.

---

## Tarefa 1 — Aprovar as questões pendentes

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** liberar para uso na plataforma as questões novas que estão corretas.

**Pré-requisitos:** ter a permissão `audit_question` ou a de administrador.

**Como fazer:**

1. No cabeçalho, clique em **Admin** e abra a aba **Auditoria de Questões**. Quem tem só a permissão de auditoria vê o painel apenas com essa aba, que já abre selecionada.
2. Em **Questões Pendentes**, o número entre parênteses é o total de questões que aguardam auditoria. A lista vem em páginas de 20, da questão mais antiga para a mais nova.
3. Confira cada questão: o título, a disciplina, o assunto, a dificuldade, a banca, o ano e o número, o enunciado, o **Texto base**, quando houver, e as alternativas. A alternativa correta aparece destacada, com **✓ Gabarito**.
4. Se algo estiver errado, corrija a questão antes de aprovar ([Tarefa 2](#tarefa-2-corrigir-uma-questao-antes-de-aprovar)).
5. Clique em **Aprovar Questão**. A mensagem *"Questão #… aprovada com sucesso!"* confirma, e a questão sai da lista.

!!! warning "A aprovação não pode ser desfeita pela tela"
    Depois de aprovada, a questão passa a ser usada no quiz e nos simulados, e a interface não tem como devolvê-la à auditoria. Para corrigir uma questão já aprovada, edite-a pela [moderação](moderacao-de-questoes.md#tarefa-2-corrigir-uma-questao-denunciada) ou pelo banco de questões.

**Observações:**

- Uma questão sem alternativa correta não pode ser aprovada. O botão **Aprovar Questão** fica desabilitado, e a tela avisa *"⚠️ Esta questão não possui alternativa correta definida no gabarito. Edite-a antes de aprovar."*
- A lista não tem filtros nem aprovação em bloco: as questões são aprovadas uma a uma, pela ordem de cadastro.
- A aprovação registra quem aprovou e quando.
- Editar uma questão já aprovada não a devolve à auditoria.

---

## Tarefa 2 — Corrigir uma questão antes de aprovar

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** acertar o texto, as alternativas, o gabarito ou a classificação de uma questão pendente antes de liberá-la.

**Pré-requisitos:** a questão estar na lista de **Questões Pendentes**.

**Como fazer:**

1. Na questão, clique em **Editar Questão**. O formulário **Editar Questão #…** se abre no lugar dela.
2. À esquerda, em **Conteúdo Puro (Markdown)**, ficam os campos da questão. À direita, a **Pré-visualização (como aparece na aplicação)** mostra a questão como os estudantes vão vê-la e se atualiza enquanto você digita.
3. Altere o que for preciso e clique em **Salvar alterações**. A mensagem *"Questão #… atualizada com sucesso."* confirma, e a questão volta à lista, ainda pendente.
4. Confira a questão corrigida e aprove-a pela [Tarefa 1](#tarefa-1-aprovar-as-questoes-pendentes).

Para desistir, clique em **Cancelar**.

**Observações:**

- A edição segue as mesmas regras da edição pelo banco de questões, descritas em [Guia do Professor — Editar uma questão](../professor/banco-de-questoes.md#tarefa-3-editar-uma-questao): exatamente uma alternativa correta, sem incluir ou remover alternativas nem trocar imagens.
- Salvar não aprova a questão. Ela continua pendente até alguém clicar em **Aprovar Questão**.

---

## Tarefa 3 — Consultar o histórico de auditoria

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** saber quem aprovou cada questão e quando.

**Pré-requisitos:** ter a permissão `audit_question` ou a de administrador.

**Como fazer:**

1. Na aba **Auditoria de Questões**, clique em **Histórico de Auditoria**.
2. Cada registro mostra o número da questão, a descrição da aprovação — no formato *"Questão #… ('título') aprovada na auditoria por …"* — e a linha **Auditado por … em …**, com a data e a hora.
3. A lista vem da aprovação mais recente para a mais antiga, em páginas de 20.

**Observações:**

- Quem aprovou aparece pelo apelido ou, se não tiver apelido, pelo e-mail.
- O histórico mostra só as aprovações. As edições feitas durante a auditoria ficam no registro de auditoria, como as demais edições de questões.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A lista de pendentes está vazia | A tela mostra *"Nenhuma questão pendente de auditoria no momento! Todas as questões estão auditadas."* Não há questões aguardando. As novas aparecem aqui assim que são cadastradas ou importadas |
| O botão **Aprovar Questão** está desabilitado | A questão não tem alternativa correta. Edite-a pela [Tarefa 2](#tarefa-2-corrigir-uma-questao-antes-de-aprovar) e marque a correta |
| *"Erro ao aprovar questão #…"* | Recarregue a página e tente de novo. Se a questão continuar na lista, confira se ela tem alternativa correta |
| Uma questão nova não aparece no quiz nem nos simulados | Ela ainda está pendente de auditoria. Aprove-a pela [Tarefa 1](#tarefa-1-aprovar-as-questoes-pendentes) |
| O link **Admin** não aparece no cabeçalho | A sua conta não tem a permissão `audit_question` nem a de administrador. Peça-a a um administrador (ver [Usuários e Permissões](usuarios-e-permissoes.md)) |
| O painel mostra só a aba **Auditoria de Questões** | A sua conta tem a permissão de auditoria, mas não a de administrador. As demais abas são exclusivas dos administradores |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tela, ações e mensagens | Código do frontend do `ifvest-monorepo` (commit `f98a6a0`): Painel Administrativo, aba Auditoria de Questões | nov/2026 |
| Regras da auditoria | `ifvest-backend/src/services/question_audit_service.py`, `src/api/v1/admin.py` e a migration `d3e4f5a6b7c8`, no `ifvest-monorepo` | nov/2026 |
| Onde as questões auditadas são usadas | `ifvest-backend/src/services/question_bank_service.py`, `quiz_filters.py`, `quiz_service.py` e `mocktests_service.py` | nov/2026 |
