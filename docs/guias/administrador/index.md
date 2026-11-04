# Guia do Administrador

Este guia documenta as tarefas de **administração** do IFVest, todas feitas no **Painel Administrativo**: acompanhar os indicadores da plataforma, conceder e revogar permissões, moderar as denúncias de erro nas questões, importar provas em lote e ligar e desligar os módulos.

!!! info "Este guia complementa os guias do Aluno e do Professor"
    A permissão de administrador passa em todas as verificações de permissão da plataforma. Quem a tem usa o IFVest como qualquer estudante e faz também todas as tarefas do professor. Este guia cobre apenas o que se soma:

    - **Tarefas de estudo** — estão no [Guia do Aluno](../aluno/index.md).
    - **Banco de questões, simulados institucionais e redação** — estão no [Guia do Professor](../professor/index.md).

!!! info "Versão documentada"
    O guia descreve o **IFVest V3**, em produção, conferido no código em outubro de 2026. Ver [Qual versão da plataforma estes guias descrevem](../index.md#qual-versao-da-plataforma-estes-guias-descrevem).

---

## Para quem é este guia

Quem administra a plataforma: a equipe que mantém o IFVest e as pessoas a quem um administrador concedeu a permissão. Nenhum conhecimento técnico é necessário para as tarefas do painel. As que exigem acesso ao servidor, como a carga de provas por linha de comando e a configuração dos valores padrão dos módulos, ficam fora deste guia.

**Permissão:** `admin_permission`. Ela é atribuída automaticamente só à conta do administrador inicial, definida na configuração do servidor. As demais contas a recebem de um administrador, na aba **Usuários e Permissões** (ver [Conceder uma permissão](usuarios-e-permissoes.md#tarefa-2-conceder-uma-permissao)).

---

## O Painel Administrativo

Para abrir o painel, clique em **Admin** no cabeçalho (`/admin`). A aba aparece só para quem tem a permissão de administrador; para os demais, o endereço do painel mostra o aviso **Acesso Restrito**.

O painel tem cinco abas:

| Aba | O que você faz nela | Página do guia |
|---|---|---|
| **Visão Geral** | Acompanhar os indicadores, os avisos e as modificações recentes | [Indicadores e Auditoria](indicadores-e-auditoria.md) |
| **Usuários e Permissões** | Encontrar usuários e conceder e revogar permissões | [Usuários e Permissões](usuarios-e-permissoes.md) |
| **Moderação de Questões** | Tratar as denúncias de erro e corrigir as questões denunciadas | [Moderação de Questões](moderacao-de-questoes.md) |
| **Importar Questões** | Importar provas em lote, a partir de um arquivo `.zip` | [Importação de Questões](importacao-de-questoes.md) |
| **Módulos (Feature Flags)** | Ligar e desligar os módulos e as funcionalidades | [Módulos](modulos.md) |

Os termos usados na plataforma estão explicados no [Glossário](../glossario.md).

---

## Como ler as tarefas deste guia

Cada tarefa segue a estrutura explicada em [Como ler as tarefas](../index.md#como-ler-as-tarefas). Todas as tarefas deste guia exigem a permissão `admin_permission`.

---

## Estrutura do guia

As páginas seguem a ordem das abas do painel.

| Página | Conteúdo | Situação |
|---|---|---|
| [Indicadores e Auditoria](indicadores-e-auditoria.md) | Indicadores, avisos, modificações dos últimos 30 dias e últimas atualizações | ✅ Disponível |
| [Usuários e Permissões](usuarios-e-permissoes.md) | Encontrar usuários, conceder e revogar permissões | ✅ Disponível |
| [Moderação de Questões](moderacao-de-questoes.md) | Tratar as denúncias e corrigir as questões denunciadas | ✅ Disponível |
| [Importação de Questões](importacao-de-questoes.md) | Importar provas em lote e acompanhar o histórico | ✅ Disponível |
| [Módulos](modulos.md) | Ligar e desligar módulos e funcionalidades | ✅ Disponível |

---

## Conformidade com as normas

Este guia integra, junto com o [Guia do Aluno](../aluno/index.md), o [Guia do Professor](../professor/index.md) e a [seção Conta](../conta/acesso.md), o item **"Documentação de Usuário"** previsto no mapeamento da **ISO/IEC/IEEE 15289:2019** adotado pelo projeto (ver [Planejamento da Documentação](../../planejamento.md)), com estrutura e conteúdo conforme a **ISO/IEC/IEEE 26514:2022**. Este é o registro dos elementos aplicados e adiados:

| Elemento da 26514 | Onde está | Situação |
|---|---|---|
| Análise de público-alvo e tarefas | Seção "Para quem é" + inventário de tarefas por aba | ✅ Aplicado |
| Informação instrucional (tarefas passo a passo) | Corpo das páginas | ✅ Aplicado |
| Informação conceitual | "O Painel Administrativo" + introdução de cada página | ✅ Aplicado |
| Avisos de cuidado antes de ações sem volta | Caixas de aviso nas tarefas de permissões, moderação, importação e módulos | ✅ Aplicado |
| Solução de problemas | Seção "Erros e situações comuns" de cada página | ✅ Aplicado |
| Mensagens de erro (textos exatos) | Nas tabelas de erros, conferidas no código | 🟡 Aplicado onde há mensagem definida |
| Informação de referência | Coberta fora do guia pela [Descrição das Funcionalidades](../../funcionalidades.md#painel-administrativo) e pela [Arquitetura](../../arquitetura.md#feature-flags) | ✅ Coberto |
| Glossário | [Glossário](../glossario.md), comum aos guias | ✅ Aplicado |
| Validação com usuários | Prevista conforme a **ISO/IEC/IEEE 26513** | ⬜ Pendente |
