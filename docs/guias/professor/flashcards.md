# Flashcards

O módulo de **Flashcards** (`/flashcards`) reúne os cartões de estudo que os alunos usam para revisar conteúdo. Cada cartão tem uma **pergunta** na frente e uma **resposta** no verso, e é classificado por área, tópico e nível de dificuldade.

Na versão atual da plataforma, **todos os flashcards disponíveis aos alunos são criados pelos professores** — o aluno estuda com os cartões cadastrados aqui.

Na versão refatorada, o **acervo da plataforma** passa a ser composto pelos cartões de professores e administradores, disponíveis a todos os alunos. Cartões que venham a ser criados por um aluno ficam restritos à conta dele e não integram esse acervo.

!!! warning "Módulo ainda não disponível no IFVest V3"
    O módulo de **Flashcards** ainda não foi implementado no IFVest V3, a versão em produção: não há telas nem rotas na API para criar cartões. O item **Flashcards** do cabeçalho fica desabilitado e, se um administrador ativar o módulo, leva à tela **Em Breve**.

    Esta página fica como **registro do que foi planejado**, a título de curiosidade:

    - as tarefas com status **✅ Atual** descrevem o módulo da **versão anterior** da plataforma, que não existe mais. Nesta página, "plataforma atual" e "versão atual" se referem a ela;
    - a seção sobre o redesign descreve a proposta do subprojeto de frontend, que pode não ser a adotada quando o módulo for implementado;
    - o campo **Perfil** e a marca 🔄 vêm da época em que a divisão de tarefas entre professor e administrador estava em discussão. No V3, o que cada conta pode fazer depende das [permissões](index.md#para-quem-e-este-guia).

    Os termos de organização dos conteúdos usados aqui — área e tópico — são os da versão anterior. A organização do V3 está no [Glossário](../glossario.md#como-os-conteudos-sao-organizados).

---

## Tarefa 1 — Criar um flashcard

**Status:** ✅ Atual  
**Perfil:** 🔄 A definir — pode ser compartilhada com o administrador

**Objetivo:** cadastrar um cartão de estudo, disponibilizando-o aos alunos.

**Pré-requisitos:** estar logado com perfil de professor; ter definidos a área e o tópico aos quais o cartão pertence.

**Como fazer:**

1. Acesse **Criar flashcard** (`/flashcards/criar`).
2. Preencha os campos:

    | Campo | Função |
    |---|---|
    | **Pergunta** | o que é exibido na frente do cartão |
    | **Resposta** | o que é exibido ao virar o cartão |
    | **Área** | área de conhecimento à qual o cartão pertence |
    | **Tópico** | categorização mais específica dentro da área |
    | **Dificuldade** | Fácil, Médio ou Difícil |

3. Salve. O cartão passa a integrar o acervo disponível aos alunos.

!!! tip "A dificuldade e o tópico são filtros para o aluno"
    Os três campos de classificação — área, tópico e dificuldade — são exatamente os filtros que o aluno usa para escolher o que revisar. Preenchê-los com cuidado é o que torna seu cartão localizável: um flashcard mal classificado dificilmente será encontrado por quem procura aquele conteúdo.

**Observações:**

- Cartões curtos e objetivos funcionam melhor no formato pergunta-resposta, que é revisado em sequência rápida — o aluno vê até 10 cartões por rodada.
- Os campos de pergunta e resposta são de texto longo, sem limite fixo de caracteres definido. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Tarefa 2 — Editar um flashcard

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** corrigir ou atualizar um cartão já cadastrado.

**Pré-requisitos:** ter o flashcard cadastrado.

**Como fazer:**

1. Localize o flashcard e acione a edição (`/flashcards/:id/editar`).
2. Altere os campos desejados — **todos** são editáveis, inclusive a área, o tópico e a dificuldade.
3. Salve as alterações.

**Observações:**

- Alterar a área, o tópico ou a dificuldade muda **em quais filtros** o cartão passa a aparecer para os alunos.
- **Não existe listagem por autor.** Diferente das questões e dos simulados, o flashcard não registra quem o criou — o acesso à edição se dá pela listagem geral de cartões. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Tarefa 3 — Excluir um flashcard

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** remover definitivamente um cartão do acervo.

**Pré-requisitos:** ter o flashcard cadastrado.

**Como fazer:**

1. Localize o flashcard e acione a exclusão.
2. O cartão é removido e deixa de aparecer para os alunos.

!!! warning "Antes de excluir, considere editar"
    Como todos os campos de um flashcard são editáveis ([Tarefa 2](#tarefa-2-editar-um-flashcard)), corrigir costuma ser preferível a excluir e recriar.

    A exclusão remove, junto com o cartão, o **registro de revisão de todos os alunos** que já o estudaram — a repetição espaçada deles perde esse histórico. A edição preserva tudo isso. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Sobre o redesign deste módulo

O redesign do módulo de Flashcards está documentado **do ponto de vista do aluno**: nova divisão em abas, navegação por disciplina, assunto e subassunto, e a possibilidade de o aluno criar seus próprios cartões — que serão **visíveis apenas na conta dele**, sem se somar ao acervo das disciplinas.

Para você, isso significa que os cartões criados aqui continuam integrando o acervo da plataforma, apresentado ao aluno na aba de flashcards pré-definidos. As telas do professor, no entanto, **não são descritas em nenhum dos relatórios consultados**.

O relatório se refere ao acervo como sendo de "professores/administradores", e a criação de cartões pelo aluno segue **em deliberação** pelo subprojeto de frontend — por isso a [Tarefa 1](#tarefa-1-criar-um-flashcard) está marcada como podendo ser compartilhada com o perfil de administrador.

⬜ *A documentar quando houver material sobre a área do professor no módulo de Flashcards: como ficarão as telas de criação, edição e exclusão, e se haverá uma listagem dos cartões de sua autoria.*

*Fonte: Relatório 4 — Isabella Pereira (frontend), redesign do módulo Flashcards.*

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| O aluno relata não encontrar meu flashcard | Confira a área, o tópico e a dificuldade do cartão: são os filtros pelos quais o aluno chega até ele |
| Não encontro o tópico adequado ao cadastrar | Crie o tópico na área correspondente antes de cadastrar o cartão — na versão anterior, pela tela **Meus tópicos** do banco de questões |
| Preciso corrigir um cartão já publicado | Use a edição — todos os campos são alteráveis, sem necessidade de excluir e recriar |
| ⬜ Mensagens de erro específicas | As mensagens exatas serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Versão anterior (Tarefas 1–3) | Campos, criação, edição e exclusão: Descrição das Funcionalidades, na versão de jun/2026, que descrevia a plataforma anterior — módulo Flashcards, seção "Para o Professor", derivada do código-fonte (rotas `/flashcards/criar`, `:id/editar`, `:id/excluir`) | jun/2026 |
| Uso pelo aluno | Filtros e limite de 10 cartões por rodada: Descrição das Funcionalidades, na versão de jun/2026 — módulo Flashcards, seção "Para o Aluno" | jun/2026 |
| Redesign do módulo (lado do aluno) | Relatório 4 — Isabella Pereira, subprojeto *Refatoração para React e Redesign do IFVest* | abr/2026 |

Nenhum dos relatórios de redesign consultados descreve as telas do professor neste módulo. A página de [Flashcards do Guia do Aluno](../aluno/flashcards.md) documenta o outro lado — como os cartões cadastrados aqui são estudados.
