# Moderação de Questões

Quando alguém encontra um erro numa questão, usa o botão **🚩 Sinalizar** para enviar uma **denúncia**, com o motivo e, se quiser, uma descrição. As denúncias chegam à aba **Moderação de Questões** do Painel Administrativo, onde o administrador confere a questão, corrige-a quando há erro e encerra a denúncia.

As denúncias podem vir dos estudantes, durante um quiz ou um simulado, e dos professores, no banco de questões (ver [Guia do Aluno — Denunciar um erro numa questão](../aluno/simulados.md#tarefa-8-denunciar-um-erro-numa-questao)). Cada uma fica numa destas situações:

| Situação | Significado |
|---|---|
| **Pendente** | Ainda não foi tratada |
| **Resolvida** | O erro foi corrigido, ou a denúncia foi atendida de outro modo |
| **Descartada** | A questão não tinha o erro apontado |

---

## Tarefa 1 — Tratar as denúncias de erro

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** encerrar as denúncias, depois de conferir a questão.

**Pré-requisitos:** ter a permissão de administrador.

**Como fazer:**

1. No Painel Administrativo, abra a aba **Moderação de Questões**. Na **Visão Geral**, o botão **Corrigir questões** leva à mesma aba.
2. A lista começa nas denúncias **Pendentes**, em páginas de 20. Os botões **Resolvidas**, **Descartadas** e **Todas** mostram as demais.
3. Cada denúncia mostra o número da questão e o motivo — por exemplo, "Questão #12: Gabarito incorreto" —, a situação, a descrição escrita por quem denunciou, quando houver, e o número da denúncia.
4. Confira a questão. Se houver erro, corrija-a pela [Tarefa 2](#tarefa-2-corrigir-uma-questao-denunciada), que pode resolver as denúncias ao salvar.
5. Para encerrar a denúncia sem editar a questão, clique em **Marcar como Resolvida** ou, se não houver erro, em **Descartar**. A mensagem *"Denúncia #… atualizada para …"* confirma.

**Observações:**

- Os botões **Marcar como Resolvida** e **Descartar** aparecem só nas denúncias pendentes. Pela tela, uma denúncia encerrada não volta a ficar pendente.
- Quem denunciou não é avisado de que a denúncia foi tratada.
- Uma mesma questão pode ter várias denúncias. Ao corrigi-la pela Tarefa 2, todas as pendentes podem ser resolvidas de uma vez.

---

## Tarefa 2 — Corrigir uma questão denunciada

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** corrigir a questão apontada numa denúncia e encerrar as denúncias dela.

**Pré-requisitos:** a questão ter ao menos uma denúncia, pendente ou não.

**Como fazer:**

1. Na aba **Moderação de Questões**, localize a denúncia e clique em **Editar questão**. O formulário **Editar Questão #…** se abre logo abaixo da denúncia, com os mesmos campos do cadastro, já preenchidos.
2. Altere o que for preciso: os dados da questão, o texto das alternativas, a alternativa correta, a resolução e a classificação.
3. Se a questão tiver denúncias pendentes, o formulário traz, já marcada, a caixa que as marca como resolvidas ao salvar — por exemplo, *"Marcar as 2 denúncias pendentes desta questão como resolvidas"*. Desmarque-a se quiser tratá-las depois.
4. Clique em **Salvar alterações**. A mensagem informa a questão atualizada e quantas denúncias foram resolvidas — por exemplo, *"Questão #12 atualizada e 2 denúncia(s) resolvida(s)."*

Para desistir, clique em **Cancelar**.

**Observações:**

- A edição segue as mesmas regras da edição pelo banco de questões, descritas em [Guia do Professor — Editar uma questão](../professor/banco-de-questoes.md#tarefa-3-editar-uma-questao): exatamente uma alternativa correta, sem incluir ou remover alternativas nem trocar imagens.
- Quem tem a permissão `edit_question` também corrige as questões pelo banco de questões, sem passar pela moderação. Por esse caminho, as denúncias da questão continuam pendentes até que um administrador as trate aqui.
- Uma questão corrigida fica protegida: uma importação posterior não desfaz a correção, a menos que o administrador peça para substituí-la (ver [Importação de Questões](importacao-de-questoes.md#tarefa-1-importar-questoes-em-lote)).

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| *"Nenhuma denúncia encontrada para este filtro."* | Não há denúncias na situação escolhida. Troque o filtro para **Todas** |
| *"Erro ao atualizar status da denúncia."* | Recarregue a página e tente de novo. A denúncia pode já ter sido tratada por outro administrador |
| *"Não foi possível contar as denúncias pendentes da questão #…"* | O formulário abre mesmo assim, mas sem a caixa de resolver as denúncias. Depois de salvar, encerre-as uma a uma |
| *"Questão #… atualizada, mas … denúncia(s) não puderam ser resolvidas."* | A questão foi salva. Encerre as denúncias que faltaram com **Marcar como Resolvida** |
| *"Não foi possível salvar a questão. Tente novamente."* | Confira a conexão e tente de novo. Se a mensagem falar das alternativas, confira se há exatamente uma correta |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tela, ações e mensagens | Código do frontend do `ifvest-monorepo` (commit `73c9098`): Painel Administrativo, aba Moderação de Questões | out/2026 |
| Regras das denúncias e da edição | [Descrição das Funcionalidades — Moderação de questões](../../funcionalidades.md#moderacao-de-questoes) e [Edição de questões](../../funcionalidades.md#edicao-de-questoes), conferidas no código do backend | out/2026 |
