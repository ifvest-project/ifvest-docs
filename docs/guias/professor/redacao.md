# Redação

No módulo de **Redação**, o professor publica as **propostas** sobre as quais os estudantes escrevem e **corrige** as redações enviadas, pelas cinco competências do ENEM. Cada parte depende de uma permissão própria:

| Tarefa | Permissão |
|---|---|
| Criar, editar e excluir propostas | `create_essay_proposal_permission` |
| Corrigir redações | `grade_essay_permission` |

Na Área do Professor, as abas **Propostas de Redação** e **Fila de Correção** aparecem para todos que entram na área. Sem a permissão correspondente, a aba mostra o aviso **Acesso Bloqueado**, com o nome da permissão que falta. A fila e a tela de correção, abertas pelo endereço, mostram nesse caso o aviso **Acesso Restrito**, também com a permissão necessária.

Escolher um tema, escrever e enviar uma redação funciona para você como para qualquer estudante, e está descrito no [Guia do Aluno — Redação](../aluno/redacao.md).

---

## Tarefa 1 — Criar uma proposta de redação

**Status:** ✅ Disponível  
**Acesso:** `create_essay_proposal_permission`

**Objetivo:** publicar um tema de redação, com instruções e textos de apoio, para os estudantes escreverem.

**Pré-requisitos:** ter a permissão `create_essay_proposal_permission`.

**Como fazer:**

1. No cabeçalho, clique em **Professor** e abra a aba **Propostas de Redação** (`/area_professor?tab=essays`). O botão **+ Criar nova proposta**, na página de Redação, leva à mesma aba.
2. Clique em **+ Criar nova proposta**. O formulário **Nova Proposta de Redação** se abre no lugar da lista.
3. Preencha os campos:

    | Campo | Como preencher |
    |---|---|
    | **Tema da Proposta** | Obrigatório, com 3 a 255 caracteres. É o título que os estudantes veem na lista |
    | **Tags / Assuntos (separados por vírgula)** | Opcional. As etiquetas viram os filtros de **Assuntos** da página de Redação. **★ Marcar como Tema da Semana** acrescenta a etiqueta "Tema da Semana" |
    | **Instruções e Comando da Proposta** | Obrigatório. O comando da redação, como na prova |

4. Para acrescentar um texto de apoio, clique em **+ Criar texto de apoio** e preencha:
    - **Título do Texto de Apoio** — opcional, como "Texto I";
    - o tipo — **Texto** ou **Figura / Imagem**;
    - **Conteúdo do Texto de Apoio**, para um texto, ou **URL da Imagem**, para uma figura, com a pré-visualização logo abaixo;
    - **Fonte (Opcional)**.

    Clique em **Adicionar Texto de Apoio**. O texto entra na lista do formulário, e **Remover** o retira. Repita para cada texto de apoio.

5. Clique em **Criar Proposta**. A mensagem *"Proposta "…" criada com sucesso!"* confirma a publicação.

Para desistir, clique em **Cancelar** ou em **Fechar Formulário**.

**Observações:**

- A proposta é publicada na hora: não há rascunho nem agendamento.
- Os textos de apoio só são gravados junto com a proposta, ao clicar em **Criar Proposta**. Eles aparecem para o estudante na ordem em que foram adicionados.
- Não há envio de imagem do computador. A figura precisa estar publicada na internet, e o campo recebe o endereço dela. Se a pré-visualização não aparecer, o endereço não leva a uma imagem.
- **Tema da semana:** na página de Redação, fica em destaque a proposta com a etiqueta "Tema da Semana" ou "Destaque", ou com "tema da semana" no tema. Se mais de uma tiver a etiqueta, o destaque vai para a mais recente, na ordem padrão da página. Para trocar o tema da semana, tire a etiqueta da proposta anterior (ver [Tarefa 2](#tarefa-2-editar-ou-excluir-uma-proposta)).

---

## Tarefa 2 — Editar ou excluir uma proposta

**Status:** ✅ Disponível  
**Acesso:** `create_essay_proposal_permission`, para as propostas que você publicou

**Objetivo:** corrigir uma proposta já publicada ou retirá-la da plataforma.

**Pré-requisitos:** ter publicado a proposta.

**Como fazer:**

1. Na aba **Propostas de Redação**, encontre a proposta. A busca **Pesquisar temas de redação...** procura no tema, nas instruções e nas etiquetas, e **▼ Ver textos de apoio** mostra os textos de cada proposta.
2. Para editar, clique em **✏️ Editar**. O formulário **Editar Proposta de Redação** se abre com os dados atuais. Altere o que for preciso e clique em **Salvar Alterações**.
3. Para excluir, clique em **🗑️ Excluir** e confirme na janela do navegador.

!!! warning "A exclusão apaga as redações enviadas"
    Excluir uma proposta apaga também **todas as redações enviadas para ela e as correções delas**, que somem de **Minhas redações** de cada estudante. A exclusão não pode ser desfeita.

**Observações:**

- Só quem publicou a proposta, ou um administrador, pode editá-la ou excluí-la. Os botões aparecem em todas as propostas, mas a ação é recusada nas de outras pessoas.
- As redações já enviadas continuam ligadas à proposta editada: estudantes e corretores passam a ver a versão nova do tema, das instruções e dos textos de apoio.

---

## Tarefa 3 — Corrigir uma redação

**Status:** ✅ Disponível  
**Acesso:** `grade_essay_permission`

**Objetivo:** avaliar uma redação pelas cinco competências do ENEM, com notas, parecer e comentários em trechos do texto.

**Pré-requisitos:** ter a permissão `grade_essay_permission`; haver redações aguardando correção.

**Como fazer:**

1. Na página de Redação, clique em **Fila de correção** (`/redacao/fila-correcao`). Pela Área do Professor, abra a aba **Fila de Correção** e clique em **Acessar Fila de Correção →**.
2. A aba **Aguardando Correção** lista as redações, das mais antigas para as mais recentes, com o tema e a data de envio. Clique em **Avaliar redação**.
3. A tela **Avaliação de Redação** mostra os textos de apoio da proposta e, em **Texto do Estudante**, a redação.
4. Para comentar um trecho, selecione-o com o mouse e clique em **✍️ Comentar trecho**. O comentário entra em **Comentários por Trecho**: escolha a competência, de **C1 - Norma Culta** a **C5 - Intervenção Social**, e escreva o apontamento para o estudante. **✕ Excluir** retira o comentário.
5. Em **Critérios de Correção (ENEM)**, dê a nota de cada competência, de **Competência 1** a **Competência 5**: de 0 a 200, de 20 em 20. Os campos começam em 120, e a **Nota Total**, de 0 a 1.000, é a soma das cinco.
6. Escreva o **Parecer Pedagógico Geral**, obrigatório, com a devolutiva para o estudante.
7. Clique em **Finalizar Correção**. A janela **Correção Concluída com Sucesso!** mostra a nota total e o número de anotações. Clique em **Ir para a Fila de Correção** ou em **Permanecer nesta página**.

!!! warning "A correção não pode ser alterada"
    Cada redação recebe uma única correção, e ela não muda depois de enviada. Confira as notas, o parecer e os comentários antes de finalizar. O estudante vê a correção assim que ela é enviada.

**Observações:**

- A fila não reserva redações: se duas pessoas abrirem a mesma, só a primeira correção enviada é aceita.
- Ninguém corrige a própria redação: as suas aparecem na fila, mas o envio é recusado.
- A fila e a tela de correção não mostram quem escreveu a redação.
- Todo comentário de trecho precisa ter texto. Um comentário vazio impede o envio da correção.
- A fila mostra até 20 redações por vez, das mais antigas para as mais recentes.

---

## Tarefa 4 — Consultar as correções que você fez

**Status:** ✅ Disponível  
**Acesso:** `grade_essay_permission`

**Objetivo:** rever as notas, o parecer e os comentários de uma correção já enviada.

**Pré-requisitos:** ter corrigido ao menos uma redação.

**Como fazer:**

1. Na **Fila de Correção**, abra a aba **Histórico de Correções Realizadas**. A lista **Minhas Correções Finalizadas** mostra cada redação que você corrigiu, com o tema, a data de envio e a nota atribuída.
2. Clique em **Ver avaliação**. A correção abre no modo de visualização, com o aviso *"Redação já avaliada anteriormente. Modo de visualização ativo."*, e o botão **Redação Já Avaliada** fica desabilitado.

**Observações:**

- O histórico mostra até 20 correções, das mais recentes para as mais antigas.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A Área do Professor mostra **Acesso Restrito** | A sua conta não tem nenhuma permissão de conteúdo ou de redação. Peça-a a um administrador |
| A aba **Propostas de Redação** mostra **Acesso Bloqueado** | A sua conta não tem a permissão `create_essay_proposal_permission`. Peça-a a um administrador |
| A aba **Fila de Correção** mostra **Acesso Bloqueado** | A sua conta não tem a permissão `grade_essay_permission`. Peça-a a um administrador |
| A fila ou a correção mostram **Acesso Restrito** | Também falta a permissão `grade_essay_permission`. Clique em **Voltar ao Início** e peça-a a um administrador |
| *"Erro ao cadastrar a proposta de redação. Tente novamente."* | Confira se o tema tem ao menos 3 caracteres. A mesma mensagem aparece quando um administrador desligou a criação de propostas em **Módulos (Feature Flags)** |
| *"Erro ao atualizar a proposta de redação. Tente novamente."* | Só quem publicou a proposta, ou um administrador, pode editá-la. Se a proposta é sua, confira a conexão e tente de novo |
| *"Erro ao excluir proposta de redação."* | Só quem publicou a proposta, ou um administrador, pode excluí-la. Se a proposta é sua, confira a conexão e tente de novo |
| A figura do texto de apoio não aparece | O endereço não leva a uma imagem, ou o site de origem não permite exibi-la. Use o endereço do próprio arquivo de imagem, terminado em `.png` ou `.jpg`, por exemplo |
| O botão **Fila de correção** não aparece | A sua conta não tem a permissão `grade_essay_permission`. Peça-a a um administrador |
| O navegador não deixa finalizar e destaca uma nota | As notas vão de 0 a 200, de 20 em 20. Corrija o valor — por exemplo, para 120 ou 140 |
| O navegador pede para preencher o parecer | O **Parecer Pedagógico Geral** é obrigatório |
| *"String should have at least 1 character"* | Um comentário de trecho está sem texto. Escreva o apontamento ou clique em **✕ Excluir** |
| *"Um usuário não pode corrigir a sua própria redação."* | A redação é sua. Deixe-a para outro corretor |
| *"Redacao ID … ja foi avaliada anteriormente."* | Outra pessoa corrigiu a redação antes de você. Volte à fila e escolha outra |
| *"Não foi possível carregar a redação. Verifique suas permissões de corretor."* | A redação não existe mais, porque excluir a proposta apaga as redações, ou a conexão falhou. Volte à fila e tente de novo |
| A fila mostra "Em Breve" | Um administrador desligou a correção de redações. Tente mais tarde |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Telas, botões, mensagens e fluxos | Código do frontend do `ifvest-monorepo` (commit `f98a6a0`): Área do Professor e páginas de Redação | nov/2026 |
| Regras das propostas, da fila e da correção | [Descrição das Funcionalidades — Redação](../../funcionalidades.md#redacao), conferida no código do backend | nov/2026 |
| Validação das notas e das correções | `ifvest-backend/src/schemas/essays.py` e `src/services/essays_service.py`, no `ifvest-monorepo` | out/2026 |
