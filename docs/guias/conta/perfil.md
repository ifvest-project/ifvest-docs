# Perfil e Seus Dados

Esta página reúne as tarefas da área de **perfil** (`/perfil`): consultar os seus indicadores, alterar o apelido e acompanhar a sua atividade no IFQuiz e nos Simulados. Ela vale para todos que têm conta.

Para abrir o perfil, clique em **Usuário**, no canto direito do cabeçalho.

---

## Tarefa 1 — Consultar o seu perfil

**Status:** ✅ Disponível  
**Acesso:** com conta

**Objetivo:** ver os dados da sua conta e o resumo do seu uso da plataforma.

**Pré-requisitos:** ter entrado na plataforma (ver [Acesso e Conta](acesso.md#tarefa-1-entrar-na-plataforma)).

**Como fazer:**

1. Clique em **Usuário**, no cabeçalho.
2. O perfil mostra o seu apelido, o e-mail da conta e três indicadores:

    | Indicador | O que mostra |
    |---|---|
    | **Pontos Totais** | O seu saldo de pontos do IFQuiz, que diminui quando você compra na [loja de avatares](../aluno/ifquiz.md#tarefa-7-comprar-e-equipar-avatares) |
    | **Dias Consecutivos** | A sua [sequência diária](../aluno/ifquiz.md#tarefa-4-manter-a-sequencia-diaria) na Pergunta do Dia |
    | **Permissões Ativas** | Quantas permissões a sua conta tem, como as de professor |

---

## Tarefa 2 — Alterar o seu apelido

**Status:** ✅ Disponível  
**Acesso:** com conta

**Objetivo:** definir o nome que identifica você na plataforma.

**Pré-requisitos:** os mesmos da [Tarefa 1](#tarefa-1-consultar-o-seu-perfil).

**Como fazer:**

1. No perfil, clique em **Editar**, ao lado do apelido.
2. Digite o novo apelido.
3. Clique em **Salvar**.

**Observações:**

- O apelido aparece na saudação da página **Início** e no [ranking do IFQuiz](../aluno/ifquiz.md#tarefa-6-ver-o-ranking). Sem apelido, a saudação usa o nome da sua conta Google, o perfil mostra "Sem apelido", e o ranking mostra a parte do seu e-mail antes do `@`.

---

## Tarefa 3 — Acompanhar a sua atividade

**Status:** ✅ Disponível  
**Acesso:** com conta

**Objetivo:** rever o que você fez no IFQuiz e nos Simulados e retomar o estudo a partir daí.

**Pré-requisitos:** os mesmos da [Tarefa 1](#tarefa-1-consultar-o-seu-perfil).

**Como fazer:**

Abaixo dos indicadores, o perfil reúne três quadros:

- **Atividade na Pergunta do Dia** — um mapa de calor do ano, com um quadrado por dia: verde para acerto, vermelho para erro e cinza para os dias sem resposta. Mostra os totais de acertos e erros e permite trocar o ano.
- **Histórico de quizzes** — os dez quizzes iniciados mais recentemente, com acertos e pontos. **Revisar** abre o gabarito do quiz, e **Refazer** abre a montagem com os mesmos filtros.
- **Histórico de Simulados** — as suas tentativas de simulado, da mais recente para a mais antiga, cinco por página, com o título, as disciplinas, a data, os acertos e a nota. **Refazer** abre o simulado de novo.

**Observações:**

- O Histórico de Simulados não aparece quando o módulo de Simulados está desligado.
- Não há revisão das questões de uma tentativa de simulado já enviada: o histórico mostra só o resultado.

---

## Previstas, ainda não disponíveis

**Status:** 🔵 Prevista

O design do subprojeto de frontend e a especificação anterior previam, na área de perfil, três tarefas que o IFVest V3 ainda não oferece:

- **Trocar a foto de perfil** — não há foto de perfil. A imagem que aparece no ranking é o avatar escolhido na loja do IFQuiz.
- **Trocar a senha** — não se aplica: o IFVest não tem senha própria, e a senha é a da sua conta Google.
- **Excluir a conta** — não há exclusão de conta pela plataforma.

*Fonte: Relatório 1 — Maria Luiza, subprojeto Refatoração para React e Redesign do IFVest, item 4; requisito [RFG03](../../requisitos/funcionais.md#rfg03).*

⬜ *A confirmar com o projeto o canal para pedir a exclusão da conta ou uma cópia dos seus dados, conforme a LGPD, enquanto a plataforma não oferecer essas opções.*

---

## Seus dados na plataforma

Da sua conta Google, o IFVest guarda **apenas o e-mail**, que identifica a sua conta. Além dele, a plataforma registra o apelido e o avatar, se você os definir, as suas permissões e os dados do seu uso: pontos, sequência diária, respostas aos quizzes, tentativas de simulado, redações enviadas e denúncias de erro em questões.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| Os indicadores aparecem zerados | A sua sessão pode ter terminado: entre de novo (ver [Acesso e Conta](acesso.md#erros-e-situacoes-comuns)) |
| A minha sequência voltou a zero | A sequência conta os dias seguidos com resposta à Pergunta do Dia. Um dia sem resposta a zera (ver [IFQuiz](../aluno/ifquiz.md#tarefa-4-manter-a-sequencia-diaria)) |
| Os meus pontos diminuíram | O saldo diminui quando você compra um avatar na loja. O ranking não é afetado pelas compras |
| Um simulado do histórico não abre com **Refazer** | Os simulados de treino criados antes de 10/10/2026 passaram a ser visíveis só para quem os criou. Se você resolveu um simulado de outra pessoa antes dessa data, a tentativa continua no histórico, mas o simulado não abre mais |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Telas, indicadores e históricos | Código do frontend do `ifvest-monorepo` (commit `d36de12`): página de perfil e quadros de histórico | out/2026 |
| Dados guardados pela plataforma | [Modelo de Dados](../../modelo-de-dados.md) | out/2026 |
| Tarefas previstas no design | Relatório 1 — Maria Luiza, subprojeto *Refatoração para React e Redesign do IFVest*, item 4 | abr/2026 |
