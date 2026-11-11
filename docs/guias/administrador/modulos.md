# Módulos

Os módulos da plataforma e algumas das suas funcionalidades podem ser ligados e desligados sem mexer no código, por meio de **feature flags** — interruptores guardados no servidor. Na aba **Módulos (Feature Flags)** do Painel Administrativo, o administrador liga e desliga cada um.

Os interruptores são estes, com as funcionalidades agrupadas sob o módulo a que pertencem:

| Interruptor | Chave | O que controla |
|---|---|---|
| **IFQuiz** | `module_quiz` | O módulo inteiro do IFQuiz |
| Pergunta do Dia | `quiz_daily_question` | A Pergunta do Dia e a sequência diária |
| Ranking | `quiz_ranking` | O ranking geral e o semanal |
| Loja de Avatares | `quiz_avatar_store` | A compra e a troca de avatares |
| Criar Quiz | `quiz_create_custom` | A montagem de quizzes pelos estudantes |
| **Redação** | `module_essays` | O módulo inteiro de Redação |
| Correção de Redações | `essays_grading` | A fila e a tela de correção |
| Criar Proposta | `essays_create_proposal` | A criação, a edição e a exclusão de propostas |
| **Simulados** | `module_mocktests` | O módulo inteiro de Simulados |
| Simulado Aleatório | `mocktests_random` | O modo aleatório da montagem de simulados |
| Exportar PDF | `mocktests_pdf_export` | Os botões **PDF** e **Gabarito** de "Meus simulados" |
| **Flashcards** | `module_flashcards` | Módulo previsto, ainda não implementado |
| **Revisão** | `module_revisao` | Módulo previsto, ainda não implementado |
| **Admin** | `module_admin` | O próprio Painel Administrativo |
| **Cadastrar Questões** | `mocktests_create_questions` | O cadastro de questões no banco, usado pelo IFQuiz e pelos Simulados |

---

## Tarefa 1 — Ligar ou desligar um módulo ou funcionalidade

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** tirar do ar, ou devolver, um módulo ou uma funcionalidade — por exemplo, durante uma manutenção.

**Pré-requisitos:** ter a permissão de administrador.

**Como fazer:**

1. No Painel Administrativo, abra a aba **Módulos (Feature Flags)**. A tela **Gerenciamento de Módulos (Feature Flags)** lista os módulos, cada um com as suas funcionalidades logo abaixo.
2. Cada linha mostra o nome, a origem do valor — **database** ou **environment** (ver [Tarefa 2](#tarefa-2-devolver-um-interruptor-ao-valor-padrao)) —, a chave entre parênteses, a descrição e o interruptor.
3. Clique no interruptor para ligar ou desligar. A lista se atualiza com o novo estado.

!!! danger "Não desligue o módulo Admin"
    Desligado, o interruptor **Admin** faz o Painel Administrativo mostrar a página **Em Breve** para todos, inclusive para os administradores. Como os interruptores ficam dentro do painel, ele não pode ser religado pela interface: é preciso pedir a quem mantém o servidor da plataforma.

**O que os usuários veem com um interruptor desligado:**

| Interruptor desligado | O que acontece |
|---|---|
| Um módulo inteiro | O link do cabeçalho fica riscado e sem clique, o cartão da página **Início** fica cinza, com o selo "Temporariamente desabilitado", e o endereço do módulo mostra a página **Em Breve** |
| Pergunta do Dia, Ranking ou Correção de Redações | A tela da funcionalidade é substituída pela página **Em Breve** |
| As demais funcionalidades | Vale para Criar Quiz, Loja de Avatares, Criar Proposta, Simulado Aleatório e Cadastrar Questões: a tela continua disponível, mas o conteúdo não carrega ou a ação é recusada. Em parte das telas, a mensagem diz que o módulo está desativado e que um administrador pode reativá-lo |
| Exportar PDF | Os botões **PDF** e **Gabarito** somem de "Meus simulados" |

**Observações:**

- Com um módulo desligado, as funcionalidades dele também ficam desligadas, e os interruptores delas ficam desabilitados.
- A mudança vale na hora no servidor. Quem está com a plataforma aberta vê a tela atualizada ao recarregar a página.
- Ligar **Flashcards** ou **Revisão** não disponibiliza esses módulos: eles ainda não foram implementados, e a tela continua **Em Breve**.
- **Cadastrar Questões** não fica sob Simulados porque o banco de questões serve também o IFQuiz.
- Toda alteração fica no registro de auditoria, com a descrição *"Módulo '…' ativado."* ou *"Módulo '…' desativado."* (ver [Indicadores e Auditoria](indicadores-e-auditoria.md#tarefa-2-acompanhar-as-modificacoes-recentes)).

---

## Tarefa 2 — Devolver um interruptor ao valor padrão

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** desfazer a alteração feita pelo painel e voltar ao valor definido na configuração do servidor.

**Pré-requisitos:** o interruptor ter sido alterado pelo painel.

A origem do valor de cada interruptor aparece ao lado do nome:

| Origem | Significado |
|---|---|
| **environment** | Vale o padrão definido na configuração do servidor |
| **database** | Vale o que foi escolhido no painel |

**Como fazer:**

1. Na aba **Módulos (Feature Flags)**, encontre o interruptor marcado como **database**.
2. Clique em **Reset**. O interruptor volta ao valor padrão, e a origem passa a **environment**.

**Observações:**

- O botão **Reset** aparece só nos interruptores alterados pelo painel.
- O valor padrão só pode ser mudado na configuração do servidor, fora do painel.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| *"Erro ao alterar o status do módulo."* | Recarregue a página e tente de novo |
| *"Erro ao restaurar o módulo."* | Recarregue a página e tente de novo |
| *"Não foi possível verificar quais módulos estão ativos. Tente de novo em instantes."* | A lista de interruptores não carregou. Clique em **Tentar de novo** |
| Liguei um módulo, mas os usuários ainda veem **Em Breve** | Peça que recarreguem a página. Se for Flashcards ou Revisão, os módulos ainda não existem |
| O interruptor de uma funcionalidade está cinza e não responde | O módulo a que ela pertence está desligado. Ligue o módulo primeiro |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tela, interruptores e mensagens | Código do frontend do `ifvest-monorepo` (commit `f98a6a0`): Painel Administrativo, aba Módulos | nov/2026 |
| Catálogo de interruptores e hierarquia | `ifvest-backend/src/services/feature_flags_service.py` e `src/api/v1/features.py`, no `ifvest-monorepo` | out/2026 |
| O que os usuários veem com cada interruptor desligado | [Descrição das Funcionalidades — Módulos desligados](../../funcionalidades.md#modulos-desligados) e [Arquitetura — Feature flags](../../arquitetura.md#feature-flags) | out/2026 |
