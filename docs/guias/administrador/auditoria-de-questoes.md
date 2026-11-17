# Auditoria de Questões

Toda questão nova entra no banco **pendente de auditoria**. Isso vale para as questões cadastradas pelos professores no banco de questões e para as trazidas pela [importação](importacao-de-questoes.md) ou pela carga feita no servidor. Uma questão pendente não aparece no IFQuiz, na Pergunta do Dia nem nos simulados. Na página **Auditoria de Questões**, quem tem a permissão de auditoria confere as questões, corrige o que for preciso e as aprova, uma a uma ou em bloco. A partir daí, elas passam a ser usadas na plataforma.

No banco de questões da Área do Professor, a lista mostra só as questões aprovadas, e um aviso informa quantas aguardam auditoria (ver [Guia do Professor — Banco de Questões](../professor/banco-de-questoes.md)).

!!! info "A auditoria tem página própria, fora do Painel Administrativo"
    A página abre pela aba **Auditoria** do cabeçalho (`/auditoria`), que aparece para quem tem a permissão `audit_question` ou a de administrador. Quem tem só a de auditoria usa a página sem ter acesso ao Painel Administrativo. O endereço antigo, `/admin?tab=audit`, leva à página nova.

!!! info "Auditoria de questões não é o registro de auditoria"
    A **auditoria de questões**, desta página, é a aprovação das questões antes de entrarem em uso. O **registro de auditoria** é o histórico das alterações feitas na plataforma, apresentado em [Indicadores e Auditoria](indicadores-e-auditoria.md). Cada aprovação também fica nesse registro.

---

## Tarefa 1 — Encontrar as questões pendentes

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** localizar as questões que aguardam auditoria, todas ou só as de uma disciplina, banca, ano ou dificuldade.

**Pré-requisitos:** ter a permissão `audit_question` ou a de administrador.

**Como fazer:**

1. No cabeçalho, clique em **Auditoria**. A página abre em **Questões Pendentes**; o número entre parênteses é o total de questões que aguardam auditoria.
2. Busque no campo **Pesquisar por título ou enunciado...** e use os filtros:

    | Filtro | O que faz |
    |---|---|
    | **Disciplina** e **Assunto** | Restringem a uma disciplina e a um assunto. O assunto só pode ser escolhido depois da disciplina |
    | **Banca** e **Ano** | Restringem à banca e ao ano da prova |
    | **Dificuldade** | De **Muito Fácil (1)** a **Muito Difícil (5)** |
    | **Ordenar por** | **Ordem de cadastro (antigas)**, o padrão; **Mais recentes cadastradas**; **Ano mais recente** ou **Ano mais antigo**; **Menor dificuldade** ou **Maior dificuldade** |

3. Confira o total à direita dos filtros, como "35 questões encontradas". **Limpar filtros** desfaz a busca, os filtros e a ordem. A lista vem em páginas de 20 questões.
4. Cada questão mostra o título, a disciplina, o assunto, a dificuldade, a banca, o ano e o número, o enunciado, o **Texto base**, quando houver, e as alternativas. A alternativa correta aparece destacada, com **✓ Gabarito**.

**Observações:**

- As opções de **Disciplina** e **Assunto** trazem toda a organização de conteúdos cadastrada. As de **Banca** e **Ano** vêm das questões já aprovadas: para encontrar uma questão pendente de uma banca ou de um ano que ainda não aparece nos filtros, use a busca por título ou enunciado.
- A lista mostra só as questões pendentes. As aprovadas ficam no banco de questões da Área do Professor.

---

## Tarefa 2 — Aprovar uma questão

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** liberar para uso na plataforma uma questão nova que está correta.

**Pré-requisitos:** a questão estar na lista de **Questões Pendentes** (ver [Tarefa 1](#tarefa-1-encontrar-as-questoes-pendentes)).

**Como fazer:**

1. Confira a questão: o enunciado, o texto base, as alternativas e a alternativa marcada como **✓ Gabarito**, além da classificação e dos dados da prova.
2. Se algo estiver errado, corrija a questão antes de aprovar ([Tarefa 4](#tarefa-4-corrigir-uma-questao-antes-de-aprovar)).
3. Clique em **Aprovar Questão**. A mensagem *"Questão #… aprovada com sucesso!"* confirma, e a questão sai da lista.

!!! warning "A aprovação não pode ser desfeita pela tela"
    Depois de aprovada, a questão passa a ser usada no quiz e nos simulados, e a interface não tem como devolvê-la à auditoria. Para corrigir uma questão já aprovada, edite-a pela [moderação](moderacao-de-questoes.md#tarefa-2-corrigir-uma-questao-denunciada) ou pelo banco de questões.

**Observações:**

- Uma questão sem alternativa correta não pode ser aprovada. O botão **Aprovar Questão** fica desabilitado, e a tela avisa *"⚠️ Esta questão não possui alternativa correta definida no gabarito. Edite-a antes de aprovar."*
- A aprovação registra quem aprovou e quando.
- Editar uma questão já aprovada não a devolve à auditoria.

---

## Tarefa 3 — Aprovar várias questões de uma vez

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** aprovar de uma só vez um conjunto de questões já conferidas, como as de uma prova inteira.

**Pré-requisitos:** ter conferido cada questão que será aprovada.

**Como fazer:**

1. Em **Questões Pendentes**, clique em **Modo de seleção múltipla**. Cada questão ganha a caixa **Selecionar para auditoria em bloco**, e aparece a barra **Modo de seleção múltipla**, com o número de questões selecionadas.
2. Marque as questões que quer aprovar, ou clique em **Selecionar todos da página** para marcar de uma vez as questões da página. O mesmo botão, como **Desmarcar todos da página**, desfaz a marcação.
3. Clique em **Aprovar selecionadas (…)**, com o número de questões entre parênteses. A mensagem *"… questão(ões) aprovada(s) com sucesso na auditoria!"* confirma, e as questões saem da lista.

Para desmarcar todas, clique em **Limpar seleção**. Para esconder as caixas, clique em **Fechar modo de seleção** ou em **Sair da seleção múltipla**.

!!! warning "A aprovação em bloco não pede confirmação"
    As questões selecionadas são aprovadas assim que você clica em **Aprovar selecionadas**, e a aprovação não pode ser desfeita pela tela. Confira cada questão antes de marcá-la: a aprovação em bloco poupa os cliques, não a conferência.

**Observações:**

- Questões sem alternativa correta não podem ser selecionadas: a caixa fica desabilitada, e **Selecionar todos da página** as deixa de fora.
- A seleção continua ao trocar de página, e o número da barra conta todas as questões marcadas, em qualquer página. Fechar o modo de seleção esconde as caixas, mas mantém as questões marcadas; para desmarcá-las, use **Limpar seleção**.
- Cada aprovação em bloco aceita até 100 questões.
- Se alguma questão do bloco não puder ser aprovada, as demais são aprovadas assim mesmo, e a mensagem informa quantas ficaram pendentes: *"… aprovada(s), … com pendência (sem gabarito ou não encontrada)."*
- Cada questão aprovada em bloco entra no histórico e no registro de auditoria como uma aprovação individual.

---

## Tarefa 4 — Corrigir uma questão antes de aprovar

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** acertar o texto, as alternativas, o gabarito ou a classificação de uma questão pendente antes de liberá-la.

**Pré-requisitos:** a questão estar na lista de **Questões Pendentes**.

**Como fazer:**

1. Na questão, clique em **Editar Questão**. O formulário **Editar Questão #…** se abre no lugar dela.
2. À esquerda, em **Conteúdo Puro (Markdown)**, ficam os campos da questão. À direita, a **Pré-visualização (como aparece na aplicação)** mostra a questão como os estudantes vão vê-la e se atualiza enquanto você digita.
3. Altere o que for preciso. A **Disciplina**, a **Matéria / Assunto** e o **Tópico** são escolhidos em listas, entre os já cadastrados.
4. Clique em **Salvar alterações**. A mensagem *"Questão #… atualizada com sucesso."* confirma, e a questão volta à lista, ainda pendente.
5. Confira a questão corrigida e aprove-a pela [Tarefa 2](#tarefa-2-aprovar-uma-questao).

Para desistir, clique em **Cancelar**.

**Observações:**

- A edição segue as mesmas regras da edição pelo banco de questões, descritas em [Guia do Professor — Editar uma questão](../professor/banco-de-questoes.md#tarefa-3-editar-uma-questao): exatamente uma alternativa correta, sem incluir ou remover alternativas nem trocar imagens.
- Salvar não aprova a questão. Ela continua pendente até ser aprovada.

---

## Tarefa 5 — Consultar o histórico de auditoria

**Status:** ✅ Disponível  
**Acesso:** `audit_question` (ou `admin_permission`)

**Objetivo:** saber quem aprovou cada questão e quando.

**Pré-requisitos:** ter a permissão `audit_question` ou a de administrador.

**Como fazer:**

1. Na página **Auditoria de Questões**, clique em **Histórico de Auditoria**.
2. Cada registro mostra o número da questão, a descrição da aprovação — no formato *"Questão #… ('título') aprovada na auditoria por …"* — e a linha **Auditado por … em …**, com a data e a hora.
3. A lista vem da aprovação mais recente para a mais antiga, em páginas de 20.

**Observações:**

- Quem aprovou aparece pelo apelido ou, se não tiver apelido, pelo e-mail.
- O histórico mostra só as aprovações. As edições feitas durante a auditoria ficam no registro de auditoria, como as demais edições de questões.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A lista de pendentes está vazia | Sem filtros, a tela mostra *"Nenhuma questão pendente de auditoria no momento! Todas as questões estão auditadas."*: não há questões aguardando. As novas aparecem aqui assim que são cadastradas ou importadas |
| *"Nenhuma questão não auditada encontrada para os filtros informados."* | Nenhuma questão pendente atende à busca e aos filtros. Clique em **Limpar filtros** |
| O botão **Aprovar Questão** está desabilitado, ou a caixa de seleção não pode ser marcada | A questão não tem alternativa correta. Edite-a pela [Tarefa 4](#tarefa-4-corrigir-uma-questao-antes-de-aprovar) e marque a correta |
| *"Erro ao aprovar questão #…"* | Recarregue a página e tente de novo. Se a questão continuar na lista, confira se ela tem alternativa correta |
| *"Erro ao executar auditoria em bloco."* | Recarregue a página: as questões que chegaram a ser aprovadas saem da lista. Confira se a seleção tem no máximo 100 questões e tente de novo com as restantes |
| *"… aprovada(s), … com pendência (sem gabarito ou não encontrada)."* | Parte do bloco foi aprovada. As que ficaram continuam na lista: corrija-as e aprove de novo |
| Uma questão nova não aparece no quiz nem nos simulados | Ela ainda está pendente de auditoria. Aprove-a pela [Tarefa 2](#tarefa-2-aprovar-uma-questao) |
| A aba **Auditoria** não aparece no cabeçalho | A sua conta não tem a permissão `audit_question` nem a de administrador. Peça-a a um administrador (ver [Usuários e Permissões](usuarios-e-permissoes.md)) |
| A página mostra **Acesso Restrito** | A sua conta não tem a permissão de auditoria. Peça-a a um administrador |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Página, filtros, seleção em bloco, ações e mensagens | Código do frontend do `ifvest-monorepo` (commit `b0a5e5f`, de 17/11/2026): página `/auditoria`, componentes e hooks da auditoria | nov/2026 |
| Regras da auditoria e da aprovação em bloco | `ifvest-backend/src/services/question_audit_service.py`, `src/api/v1/admin.py` e a migration `d3e4f5a6b7c8`, no `ifvest-monorepo` | nov/2026 |
| Opções dos filtros | `ifvest-backend/src/services/question_bank_service.py`, no `ifvest-monorepo` | nov/2026 |
| Onde as questões auditadas são usadas | `ifvest-backend/src/services/question_bank_service.py`, `quiz_filters.py`, `quiz_service.py` e `mocktests_service.py` | nov/2026 |
