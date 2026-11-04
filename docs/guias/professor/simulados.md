# Simulados

No módulo de **Simulados** (`/simulados`), o que se soma para o professor é o **simulado institucional**: um simulado que você publica e que aparece para todos os estudantes. Montar simulados de treino, resolvê-los, revisá-los e imprimi-los funciona para você como para qualquer estudante, e está descrito no [Guia do Aluno — Simulados](../aluno/simulados.md).

Os simulados são montados com as questões do [Banco de Questões](banco-de-questoes.md). Os dois tipos se diferenciam assim:

| | De treino | Institucional |
|---|---|---|
| **Quem cria** | Qualquer pessoa com conta | Quem tem `create_institutional_mocktest` |
| **Quem vê e resolve** | Só quem o criou | Todos os usuários |
| **Quem edita ou exclui** | Quem o criou e quem tem `manage_mocktests` | Quem o criou e quem tem `manage_mocktests` |

---

## Tarefa 1 — Criar um simulado institucional

**Status:** ✅ Disponível  
**Acesso:** `create_institutional_mocktest`

**Objetivo:** publicar um simulado que aparece na lista de todos os estudantes.

**Pré-requisitos:** ter a permissão `create_institutional_mocktest`; as questões desejadas estarem no banco.

**Como fazer:**

1. No cabeçalho, clique em **Simulados** e, na página do módulo, em **Criar novo simulado**.
2. Preencha o **Nome do simulado**, com até 120 caracteres, e a **Quantidade de questões**. O nome é o que os estudantes verão na lista.
3. Marque **Simulado institucional**. A opção só aparece para quem tem a permissão.
4. Escolha como montar o simulado — **Aleatório**, para sortear, ou **Selecionar questões**, para escolher no banco — e siga os mesmos passos do [simulado de treino](../aluno/simulados.md#tarefa-1-montar-um-simulado-de-treino).
5. A confirmação **Simulado criado com sucesso!** traz a mensagem *"O simulado institucional foi gerado e já aparece para todos os usuários."* Se a mensagem falar em *"seus materiais de estudo"*, o simulado foi criado como de treino.

**Observações:**

- Marque a opção **antes** de escolher o modo de montagem. Depois de criado, um simulado não passa de treino a institucional, nem o contrário.
- Depois de criado, o simulado aceita só a retirada de questões, e não o acréscimo (ver [Tarefa 2](#tarefa-2-editar-ou-excluir-um-simulado-de-outra-pessoa)). Confira a seleção antes de salvar.
- Na lista **Ver meus simulados**, o simulado aparece com o selo **Institucional**. Um nome claro, que indique o vestibular ou o conteúdo, ajuda os estudantes a encontrá-lo.
- O simulado aparece também para os outros professores.

!!! warning "O gabarito fica disponível para todos"
    Todo estudante que vê o simulado pode abrir o **Gabarito** na lista e conferir a resposta de cada questão ao resolvê-lo na plataforma. Leve isso em conta antes de usar um simulado institucional como avaliação.

---

## Tarefa 2 — Editar ou excluir um simulado de outra pessoa

**Status:** ✅ Disponível  
**Acesso:** `manage_mocktests`

**Objetivo:** corrigir o nome de um simulado institucional criado por outra pessoa, tirar questões dele ou retirá-lo da plataforma.

**Pré-requisitos:** ter a permissão `manage_mocktests`.

**Como fazer:**

1. Na página de Simulados, clique em **Ver meus simulados** e, no simulado, em **Editar**.
2. Para renomear, em **1. Renomear simulado**, digite o novo nome, com até 120 caracteres, e clique em **Salvar novo nome**.
3. Para tirar questões, em **2. Questões**, clique em **Remover** em cada questão que vai sair e depois em **Salvar questões**.
4. Para excluir, em **3. Excluir simulado**, clique em **Excluir este simulado** e, em seguida, em **Confirmar exclusão**.

!!! warning "A exclusão apaga todas as tentativas"
    Excluir um simulado apaga também **as tentativas de todos os estudantes** que o resolveram, e elas somem do histórico e das estatísticas de cada um. A exclusão não pode ser desfeita.

**Observações:**

- A lista mostra só os simulados que você criou e os institucionais. Os simulados de treino dos estudantes não aparecem, mesmo com a permissão.
- Tirar questões de um simulado institucional não muda as tentativas já enviadas pelos estudantes: a nota de cada uma continua a mesma.
- Os simulados que você mesmo criou podem ser editados e excluídos sem a permissão, como descrito no [Guia do Aluno](../aluno/simulados.md#tarefa-7-editar-ou-excluir-um-simulado).

---

## Tarefa 3 — Imprimir um simulado para aplicação em papel

**Status:** ✅ Disponível  
**Acesso:** com conta

**Objetivo:** gerar o caderno de prova e a folha de gabarito de um simulado.

**Pré-requisitos:** ter o simulado na sua lista.

**Como fazer:**

1. Em **Ver meus simulados**, clique em **PDF** para abrir o caderno, com campos para os dados do candidato, instruções, as questões em duas colunas e uma folha de respostas.
2. Clique em **IMPRIMIR / SALVAR CADERNO EM PDF** para imprimir ou salvar o arquivo.
3. Para a correção, clique em **Gabarito**, na mesma lista, e em **IMPRIMIR / SALVAR GABARITO EM PDF**.

Os detalhes estão em [Imprimir o caderno e o gabarito](../aluno/simulados.md#tarefa-6-imprimir-o-caderno-e-o-gabarito), no Guia do Aluno.

**Observações:**

- A plataforma não registra as respostas dadas no papel: a nota da prova impressa é calculada fora dela, com o gabarito.
- Os botões **PDF** e **Gabarito** podem estar ocultos, se um administrador tiver desligado a exportação em **Módulos (Feature Flags)**.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A opção **Simulado institucional** não aparece | A sua conta não tem a permissão `create_institutional_mocktest`. Peça-a a um administrador |
| Criei o simulado sem marcar a opção institucional | Ele ficou como simulado de treino, visível só para você. Crie outro com a opção marcada e, se quiser, exclua o anterior |
| Preciso trocar uma questão de um simulado institucional | Não é possível acrescentar questões, só tirá-las. Se o problema estiver na própria questão, corrija-a no banco (ver [Editar uma questão](banco-de-questoes.md#tarefa-3-editar-uma-questao)): a correção vale para todos os simulados que a usam. Senão, crie outro simulado |
| O botão **Editar** não aparece num simulado institucional | O simulado é de outra pessoa, e a sua conta não tem a permissão `manage_mocktests`. Peça-a a um administrador |
| Quero ver as notas dos estudantes num simulado institucional | A plataforma não mostra ao professor os resultados dos estudantes: cada um vê apenas a própria nota e a própria revisão |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Telas, botões, mensagens e fluxos | Código do frontend do `ifvest-monorepo` (commit `73c9098`): páginas de Simulados | out/2026 |
| Regras de acesso, criação, edição e exclusão | [Descrição das Funcionalidades — Simulados](../../funcionalidades.md#simulados), conferida no código do backend | out/2026 |
| Simulados institucionais e de treino | `docs/auditoria-simulados-2026-10-10.md`, no `ifvest-monorepo` | out/2026 |

!!! note "O que mudou em relação ao planejado"
    A versão anterior desta página descrevia a criação de simulados da plataforma anterior, restrita aos professores, com **descrição** obrigatória, escolha do **tipo** — objetivo, dissertativo ou aleatório — e telas para **adicionar e remover questões** depois da criação. No V3, qualquer pessoa monta simulados de treino, o professor publica os institucionais, e depois da criação as questões podem ser retiradas, mas não acrescentadas.

    O redesign previa ainda a escolha do **tipo de simulado** — por disciplina, por assunto, ENEM ou UNICAMP — e do **tipo de questão**, além de um **atalho** para o simulado recém-criado. O tipo de simulado virou a combinação de filtros do modo aleatório — disciplina, assunto, banca e ano —, e não há questões dissertativas: o banco do V3 tem só questões de múltipla escolha.

    *Fontes: Relatórios 2 e 3 — Isabella Pereira e Fluxograma sugerido, subprojeto Refatoração para React e Redesign do IFVest (mar–abr/2026).*
