# Indicadores e Auditoria

A aba **Visão Geral** é a primeira do Painel Administrativo. Ela reúne os indicadores da plataforma, os avisos que pedem atenção, o pódio do IFQuiz e o resumo do **registro de auditoria**, que guarda quem fez cada alteração de conteúdo e de configuração.

---

## Tarefa 1 — Acompanhar os indicadores da plataforma

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** ver, de relance, o tamanho da plataforma e o que precisa de atenção.

**Pré-requisitos:** ter a permissão de administrador.

**Como fazer:**

1. No cabeçalho, clique em **Admin**. O painel abre na aba **Visão Geral**.
2. Confira os indicadores do topo:

    | Indicador | O que mostra | Botão |
    |---|---|---|
    | **Usuários cadastrados** | O total de contas e, abaixo, as criadas nos últimos 7 dias, como "+3 essa semana" | — |
    | **Questões no banco** | O total de questões do banco, incluindo as pendentes de auditoria | **Ver banco de questões**, que abre o Banco de Questões da Área do Professor |
    | **Simulados** | O total de simulados, de treino e institucionais | **Ver banco de simulados**, que abre a página de Simulados |
    | **Questões sinalizadas** | As denúncias de erro ainda pendentes | **Corrigir questões**, que abre a [Moderação de Questões](moderacao-de-questoes.md) |
    | **Permissões** | O total de permissões concedidas, somando todas as contas | **Configurar**, que abre [Usuários e Permissões](usuarios-e-permissoes.md) |

3. Em **Avisos**, aparecem os pontos que pedem atenção: as denúncias aguardando moderação e o banco de questões vazio. Sem pendências, o quadro não aparece.
4. O quadro **Ranking Geral - IFQuiz** mostra os três estudantes com mais pontos ganhos no IFQuiz, pelo mesmo critério do [ranking geral](../aluno/ifquiz.md#tarefa-6-ver-o-ranking).

**Observações:**

- Os números são os do momento em que o painel abriu. Para atualizá-los, recarregue a página.
- O indicador **Simulados** conta também os simulados de treino, que só os próprios estudantes veem.

---

## Tarefa 2 — Acompanhar as modificações recentes

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** saber o que foi alterado na plataforma e por quantas pessoas, a partir do registro de auditoria.

**Pré-requisitos:** ter a permissão de administrador.

**Como fazer:**

1. Na aba **Visão Geral**, o quadro **Modificações - Últimos 30 dias** mostra:

    | Número | O que conta |
    |---|---|
    | **modificações** | Todas as alterações registradas no período, sem contar as denúncias feitas pelos estudantes |
    | **administradores ativos** | As pessoas com permissão de administrador que fizeram alguma alteração no período |
    | **Questões adicionadas** | As questões cadastradas uma a uma no período, pelo formulário do banco de questões. As que entram pela importação não contam aqui |
    | **Questões removidas** | As questões excluídas no período |

2. Em **Relatório mais recente**, leia a descrição da última alteração.
3. O quadro **Últimas atualizações** lista os cinco registros mais recentes, com a descrição e a data.

**Observações:**

- O registro de auditoria guarda o cadastro, a edição e a denúncia de questões, a aprovação delas na [Auditoria de Questões](auditoria-de-questoes.md), as mudanças de situação das denúncias, a criação, a edição e a exclusão de propostas de redação, a concessão e a revogação de permissões, as alterações dos módulos, as questões atualizadas pela carga a partir da fonte e as importações aplicadas pelo painel.
- Não são registrados as correções de redação, os simulados e as compras na loja do IFQuiz.
- As denúncias dos estudantes aparecem em **Últimas atualizações**, mas não contam como modificação.
- **Questões removidas** fica em zero, porque a plataforma não tem exclusão de questões.
- O painel mostra só esse resumo: não há consulta ao registro completo pela interface.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A aba **Admin** não aparece no cabeçalho | A sua conta não tem a permissão de administrador. Se ela foi concedida há pouco, recarregue a página |
| O painel mostra **Acesso Restrito** | A sua conta não tem a permissão de administrador nem a de auditoria |
| O painel mostra só a aba **Auditoria de Questões** | A sua conta tem a permissão `audit_question`, mas não a de administrador. A Visão Geral é exclusiva dos administradores |
| *"Não foi possível carregar as métricas do painel. Tente novamente mais tarde."* | Recarregue a página. Se a mensagem continuar, avise quem mantém o servidor da plataforma |
| O painel mostra a página **Em Breve** | O módulo **Admin** foi desligado em **Módulos (Feature Flags)**. Ver o aviso em [Ligar ou desligar um módulo](modulos.md#tarefa-1-ligar-ou-desligar-um-modulo-ou-funcionalidade) |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tela, indicadores e quadros | Código do frontend do `ifvest-monorepo` (commit `f98a6a0`): Painel Administrativo, aba Visão Geral | nov/2026 |
| Cálculo dos indicadores, da janela de 30 dias e dos avisos | `ifvest-backend/src/services/admin_service.py`, no `ifvest-monorepo` | nov/2026 |
| O que o registro de auditoria guarda | [Descrição das Funcionalidades — Registro de auditoria](../../funcionalidades.md#registro-de-auditoria) | nov/2026 |
