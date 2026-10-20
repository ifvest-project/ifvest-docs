# Descrição das Funcionalidades

Esta página descreve o que a plataforma faz hoje, módulo por módulo: cada funcionalidade, quem pode usá-la, onde ela fica na interface e as regras que o sistema aplica. A visão geral dos módulos está na [Descrição do Sistema](descricao-do-sistema.md), e o contrato técnico de cada operação, na [Referência da API](api.md).

!!! info "Levantada do código em produção"
    O conteúdo foi conferido no código do `ifvest-monorepo` — backend e frontend — na versão de outubro de 2026 (commit `48ad5ea`). Quando a interface e a API se comportam de formas diferentes, a página descreve as duas e indica a diferença.

    ⬜ *A correspondência entre cada funcionalidade e os requisitos será registrada quando a nova especificação de requisitos estiver concluída.*

---

## Como ler esta página

Cada funcionalidade traz, logo abaixo do título, três informações:

- **Acesso** — quem pode usar: *pública*, quando dispensa conta; *com conta*, para qualquer usuário que entrou na plataforma; ou a **permissão** exigida. Quem tem a permissão de administrador passa em todas as verificações. O catálogo de permissões está em [Arquitetura — Permissões](arquitetura.md#permissoes).
- **Onde** — o caminho na interface e o endereço da tela.
- **Flag** — a *feature flag* que liga e desliga a funcionalidade, além da flag do próprio módulo. O que acontece quando uma delas está desligada está em [Módulos desligados](#modulos-desligados).

## Visão geral

| Módulo | Funcionalidade | Acesso |
|---|---|---|
| Conta | Entrar com a conta Google, sair, página inicial e perfil | Com conta |
| IFQuiz | Quiz personalizado, Pergunta do Dia, sequência diária, pontos e patentes, ranking e loja de avatares | Com conta |
| Simulados | Simulado de treino, manual ou aleatório; lista, resolução, caderno em PDF e estatísticas | Com conta |
| Redação | Temas de redação | Pública |
| Redação | Escrita e envio, minhas redações | Com conta |
| Redação | Propostas de redação | `create_essay_proposal_permission` |
| Redação | Correção de redações | `grade_essay_permission` |
| Banco de questões | Consulta e denúncia de erro | Com conta |
| Banco de questões | Cadastro de questões | `create_question` |
| Banco de questões | Edição de questões | `edit_question` |
| Gestão | Área do Professor | Qualquer permissão de conteúdo ou de redação |
| Gestão | Painel Administrativo | `admin_permission` |

---

## Conta e acesso

### Entrar com a conta Google

**Acesso:** pública · **Onde:** botão "Entrar" da página inicial (`/login`)

A entrada é feita exclusivamente com a **conta Google**, numa janela do Google aberta pelo navegador. Não há cadastro com e-mail e senha: a tela de entrada tem um único botão do Google, com o rótulo "Cadastrar com Google" ou "Entrar com Google" conforme o modo escolhido no painel ao lado, e os dois fazem a mesma coisa.

No **primeiro acesso**, a plataforma cria a conta a partir do e-mail da conta Google e atribui as permissões iniciais conforme esse e-mail — as regras estão em [Descrição do Sistema — Como as permissões são atribuídas](descricao-do-sistema.md#como-as-permissoes-sao-atribuidas). Nos acessos seguintes, a conta é reconhecida pelo mesmo e-mail. Depois de entrar, o usuário é levado à página Início.

### Sair

**Acesso:** com conta · **Onde:** botão "Sair", no rodapé das telas internas

Encerra a sessão no navegador e volta para a página inicial pública.

### Início

**Acesso:** com conta · **Onde:** logotipo ou aba "Início" do cabeçalho (`/inicio`)

Painel de entrada, com uma saudação pelo apelido e um cartão para cada módulo: Flashcards, IFQuiz, Redação, Revisão e Simulados. A Área do Professor e o Painel Administrativo não têm cartão: aparecem como abas do cabeçalho para quem tem permissão.

### Perfil

**Acesso:** com conta · **Onde:** "Usuário", no canto direito do cabeçalho (`/perfil`)

- Mostra o apelido, o e-mail e três indicadores: **pontos** (o saldo atual), **dias consecutivos** (a [sequência diária](#sequencia-diaria)) e **permissões ativas**.
- O **apelido** pode ser editado. É o nome exibido no ranking; sem apelido, o ranking mostra a parte do e-mail antes do `@`.
- **Atividade na Pergunta do Dia** — mapa de calor do ano, com um quadrado por dia: verde para acerto, vermelho para erro e cinza para os dias sem resposta. Mostra os totais de acertos e erros e permite trocar o ano.
- **Histórico de quizzes** — os dez quizzes iniciados mais recentemente, com acertos e pontos, e as ações *Revisar*, que abre o gabarito, e *Refazer*, que abre a montagem com os mesmos filtros.

Não há foto de perfil nem exclusão de conta.

---

## IFQuiz

Módulo de prática rápida com elementos de jogo. **Flag do módulo:** `module_quiz`.

A página do módulo (`/quiz`) reúne os indicadores do estudante — saldo de pontos, dias de sequência, taxa de acertos e posição no ranking geral —, o acesso aos modos de jogo, uma prévia da Pergunta do Dia, os três primeiros do ranking da semana e a tabela de patentes.

### Quiz personalizado

**Acesso:** com conta · **Onde:** IFQuiz → "Jogar agora" ou "Prática Livre" (`/quiz/criar`) · **Flag:** `quiz_create_custom`

**Montagem.** O estudante define:

- **Nome** — opcional; sem nome, o quiz se chama "Quiz Geral" ou "Quiz de {disciplina}".
- **Disciplina** — "Geral", que reúne todas, ou uma das disciplinas que têm questões no banco, com a contagem de cada uma.
- **Assuntos** — opcionais, vários ao mesmo tempo, dentro da disciplina escolhida.
- **Quantidade** — 5, 10, 15 ou 20 questões. As opções maiores que o número de questões disponíveis no filtro ficam desabilitadas.

Não há escolha de dificuldade: o seletor foi ocultado por decisão da equipe, porque a dificuldade registrada nas questões ainda não reflete a real (ver [Modelo de Dados — Pontos de atenção](modelo-de-dados.md#pontos-de-atencao-do-modelo)). Antes de começar, uma prévia mostra o tempo estimado, de 2 minutos por questão, e os pontos possíveis.

**Partida.**

- As questões aparecem uma de cada vez, sorteadas entre as do filtro.
- O estudante tem **3 vidas**. Cada erro custa uma, e o quiz termina no terceiro erro ou quando todas as questões forem respondidas.
- A **dica** elimina uma alternativa errada, uma vez por questão, e não pode ser usada quando resta só uma vida.
- Depois de confirmar, a tela mostra se a resposta está certa e qual é a alternativa correta.
- Não há cronômetro. Cada acerto vale 20 pontos, independentemente da sequência de acertos (*combo*) mostrada na tela.

**Resultado e revisão.** Ao final, os pontos — **20 por acerto** — são somados ao saldo. A tela de resultado mostra os pontos ganhos, os acertos, os erros, as vidas restantes e o progresso até a próxima [patente](#pontos-e-patentes). A revisão lista as questões respondidas, com a alternativa escolhida e o gabarito oficial.

Durante a partida, o botão "Sinalizar" permite [denunciar um erro](#denuncia-de-erro) na questão.

### Pergunta do Dia

**Acesso:** com conta · **Onde:** IFQuiz → "Pergunta do dia" (`/quiz/pergunta-do-dia`) · **Flag:** `quiz_daily_question`

- **Uma questão por dia, a mesma para todos**, escolhida a partir da data, no horário de Brasília.
- **Uma resposta por dia.** Depois de responder, as alternativas ficam bloqueadas até o dia seguinte.
- O acerto vale **100 pontos**, creditados na hora.
- O resultado mostra a alternativa correta, a sequência diária e o **desempenho da comunidade**: o percentual de acerto de todos que responderam e a distribuição das respostas por alternativa.
- Na tela de resultado, o botão "Jogar Quiz Rápido" inicia direto um quiz de 5 questões de todas as disciplinas, sem passar pela montagem.

### Sequência diária

**Acesso:** com conta · **Onde:** indicadores do IFQuiz e do Perfil

- Conta os dias seguidos, no horário de Brasília, em que o estudante **respondeu à Pergunta do Dia**, acertando ou não.
- Responder a quizzes ou apenas entrar na plataforma não conta.
- Um dia sem resposta zera a sequência, e a resposta seguinte a recomeça em 1.
- A sequência não rende pontos extras.

### Pontos e patentes

Os pontos vêm de duas fontes: **20 por acerto** no quiz e **100 por acerto** na Pergunta do Dia. Eles formam o **saldo**, que diminui quando o estudante compra itens na [loja](#loja-de-avatares).

A patente é definida pelo saldo, em sete níveis:

| Patente | Pontos |
|---|---|
| Bronze | 0 a 499 |
| Prata | 500 a 999 |
| Ouro | 1.000 a 1.999 |
| Platina | 2.000 a 3.499 |
| Diamante | 3.500 a 4.999 |
| Mestre | 5.000 a 7.499 |
| Lenda do IF | 7.500 ou mais |

Como depende do saldo, a patente **pode cair quando o estudante compra na loja**. O ranking, por sua vez, não é afetado pelas compras.

### Ranking

**Acesso:** com conta · **Onde:** IFQuiz → "Ver tudo" no ranking semanal (`/quiz/ranking`) · **Flag:** `quiz_ranking`

- Dois períodos: **geral**, com todo o histórico, e **semanal**, contado a partir de segunda-feira à 0h, no horário de Brasília.
- A classificação usa os **pontos ganhos** — quizzes concluídos e acertos da Pergunta do Dia —, e não o saldo: compras na loja não fazem o estudante perder posição.
- Só entra quem tem pontos no período. Empates dividem a mesma posição.
- A tela mostra a posição do próprio estudante, o pódio com os três primeiros, quando há ao menos três classificados, e a tabela com avatar, patente e sequência de cada um. A interface exibe apenas os dez primeiros colocados.

### Loja de avatares

**Acesso:** com conta · **Onde:** IFQuiz → "Loja de Avatares" (`/quiz/loja`) · **Flag:** `quiz_avatar_store`

Avatares cosméticos, comprados com o saldo de pontos:

| Avatar | Preço |
|---|---|
| 🎓 Calouro IF | Gratuito |
| 🦉 Sábio dos Vestibulares | 200 pontos |
| 🚀 Foguete Estudante | 400 pontos |
| ⚡ Mente Rápida | 600 pontos |
| 💎 Mestre da Física | 800 pontos |
| 👑 Rei do Quiz | 1.200 pontos |

Cada avatar é comprado uma única vez, e a compra exige saldo suficiente. Depois de comprado, o avatar pode ser **equipado** e passa a aparecer no ranking; o gratuito pode ser equipado sem compra.

---

## Simulados

Treino com conjuntos de questões do banco, resolvidos na plataforma ou impressos. **Flag do módulo:** `module_mocktests`.

### Página de simulados e estatísticas

**Acesso:** com conta · **Onde:** aba "Simulados" do cabeçalho (`/simulados`)

Dá acesso à lista de simulados e à criação de um novo, e mostra as **estatísticas** do estudante: o total de questões respondidas e de acertos em todos os simulados enviados.

### Montar simulado de treino

**Acesso:** com conta · **Onde:** Simulados → "Criar novo simulado" (`/simulados/novo`)

O estudante dá um nome ao simulado e escolhe uma de duas formas de montá-lo:

- **Selecionar questões** — busca no banco por título ou enunciado, em páginas de 25 questões. A seleção não tem limite e é mantida entre as páginas.
- **Aleatório** (flag `mocktests_random`) — sorteia a quantidade pedida, de todas as disciplinas ou de uma destas: Língua Portuguesa, Matemática, História, Geografia, Biologia, Física ou Química. A quantidade padrão é de 10 questões. Se o filtro não tiver questões suficientes, a criação é recusada com a informação de quantas existem.

O simulado criado fica salvo na plataforma e aparece na [lista de simulados](#lista-de-simulados).

!!! note "Simulados montados por professores"
    A API prevê simulados montados por quem tem a permissão `create_mocktest`, mas a interface não oferece essa opção: hoje, todo simulado criado pela interface é um simulado de treino, que qualquer estudante pode montar. A API aceita, no simulado aleatório, filtros por assunto, dificuldade e banca, também não oferecidos na interface.

### Lista de simulados

**Acesso:** com conta · **Onde:** Simulados → "Ver meus simulados" (`/simulados/meus-simulados`)

A lista, chamada "Meus simulados", mostra **todos os simulados da plataforma**, inclusive os de treino criados por outros estudantes, com o número de questões e a nota da última tentativa do próprio usuário. A busca por nome é feita na própria tela.

Cada simulado tem três ações:

- **Resolver** — abre a resolução.
- **Editar** — permite renomear ou excluir o simulado. Só o criador, quem tem a permissão `manage_mocktests` ou um administrador podem fazer isso. Excluir um simulado apaga também **as tentativas de todos os estudantes** nele.
- **PDF** — gera o [caderno de questões](#caderno-em-pdf).

### Resolver simulado

**Acesso:** com conta · **Onde:** "Resolver", na lista de simulados (`/simulados/resolver/{id}`)

- As questões aparecem uma de cada vez, com banca, ano e dificuldade (de 1 a 5), e é possível avançar e voltar.
- Ao confirmar uma resposta, a tela mostra na hora se ela está certa.
- **Finalizar simulado** envia o conjunto, sem pedir confirmação. A nota é a proporção de acertos sobre o total de questões, de 0 a 100: questões em branco contam como erradas.
- Cada envio registra uma tentativa, com o total de questões, as respondidas, os acertos e a nota. As tentativas são ilimitadas e não rendem pontos.
- Não há revisão das questões depois de finalizar.
- O botão "Sinalizar" permite [denunciar um erro](#denuncia-de-erro) na questão.

### Caderno em PDF

**Acesso:** com conta · **Onde:** "PDF", na lista de simulados · **Flag:** `mocktests_pdf_export`, sem efeito na interface

Abre, numa nova janela, o caderno do simulado: campos para os dados do candidato, instruções, as questões em duas colunas e uma folha de respostas com as alternativas de A a E para marcar. O botão "IMPRIMIR / SALVAR CADERNO EM PDF" abre a impressão do navegador, que permite salvar o arquivo. O caderno não traz o gabarito.

O caderno é montado **pelo próprio navegador**, sem usar a exportação em PDF da API. Por isso, a flag `mocktests_pdf_export`, que controla essa exportação, não afeta o caderno.

---

## Redação

Treino de redação com propostas temáticas e correção pela grade do ENEM. **Flag do módulo:** `module_essays`.

### Temas de redação

**Acesso:** pública · **Onde:** aba "Redação" do cabeçalho (`/redacao`)

- Lista as propostas, com busca pelo tema e pelas instruções, ordenação das mais recentes ou das mais antigas e filtro pelas etiquetas de assunto. A interface carrega as 20 primeiras propostas.
- **Tema da semana** — fica em destaque a primeira proposta com a etiqueta "Tema da Semana" ou "Destaque", ou com "tema da semana" no título; se nenhuma tiver, a primeira da lista.
- Cada tema indica se o estudante já enviou uma redação para ele e leva à escrita ou, depois do envio, à lista de [redações do estudante](#minhas-redacoes).
- Para quem tem permissão, a tela mostra também os acessos à [fila de correção](#correcao-de-redacoes) e à [criação de propostas](#propostas-de-redacao).

### Escrever e enviar redação

**Acesso:** com conta · **Onde:** "Escrever redação", num tema (`/redacao/escrever/{id}`)

- A tela apresenta o tema, as instruções e os textos de apoio, escritos ou em imagem, com a fonte de cada um.
- O editor conta as linhas digitadas, as palavras e as **linhas estimadas no papel**, sobre o limite de 30 da folha do ENEM, a partir de uma média de caracteres por linha que o estudante pode ajustar.
- **Rascunho automático** — o texto é salvo no navegador um segundo depois de cada alteração e restaurado ao voltar à tela, se o rascunho tiver menos de 10 minutos. O rascunho fica só naquele navegador.
- **Envio** — exige ao menos 10 caracteres e não tem limite máximo. A redação entra na fila de correção, como aguardando correção.
- Depois do primeiro envio, o tema passa a levar à lista de redações do estudante, e a interface não oferece um novo envio. A API aceita mais de uma redação por tema, sem limite.
- O envio de redação por arquivo, com reconhecimento do texto (OCR), aparece como "Em breve" e está desabilitado.

### Minhas redações

**Acesso:** com conta · **Onde:** Redação → "Minhas redações" (`/redacao/minhas-redacoes`)

Separa as redações **aguardando correção** das **corrigidas**, com a nota total de cada uma, de 0 a 1.000. O **espelho de correção** mostra as notas das cinco competências, o parecer do corretor e o texto com os trechos comentados destacados na cor de cada competência, acompanhados dos comentários.

### Propostas de redação

**Acesso:** `create_essay_proposal_permission` · **Onde:** Área do Professor → "Propostas de Redação" (`/area_professor?tab=essays`) · **Flag:** `essays_create_proposal`

- **Criar** — tema e instruções, obrigatórios na interface (a API exige apenas o tema, com 3 a 255 caracteres); etiquetas de assunto, separadas por vírgula, com um botão que acrescenta a etiqueta "Tema da Semana"; e textos de apoio, cada um com título, tipo — texto ou imagem — e fonte.
- As imagens são informadas **pelo endereço** de uma imagem publicada na web: não há envio de arquivo.
- **Editar e excluir** — permitido só ao autor da proposta ou a um administrador. Excluir uma proposta apaga também **todas as redações enviadas para ela e suas correções**. A tela pede confirmação antes de excluir.

### Correção de redações

**Acesso:** `grade_essay_permission` · **Onde:** Redação → "Fila de correção" (`/redacao/fila-correcao`), também acessível pela Área do Professor · **Flag:** `essays_grading`

**Fila.** Lista as redações aguardando correção, das mais antigas para as mais recentes; a interface exibe as 20 primeiras. Uma segunda aba mostra as correções já feitas pelo próprio corretor. A fila não reserva redações: duas pessoas podem abrir a mesma, e só a primeira correção enviada é aceita.

**Tela de correção.**

- Mostra os textos de apoio da proposta e o texto do estudante.
- Ao selecionar um trecho com o mouse, o corretor pode **comentá-lo**, indicando a competência: C1 – Norma Culta, C2 – Tema e Repertório, C3 – Argumentação, C4 – Coesão Textual ou C5 – Intervenção Social.
- Cada competência recebe uma nota **de 0 a 200, de 20 em 20**; o formulário começa em 120. A nota total é a soma, de 0 a 1.000.
- O parecer geral é obrigatório na interface.

**Regras.**

- Cada redação recebe **uma única correção**, e ela não pode ser alterada depois de enviada.
- **Ninguém corrige a própria redação**: a fila mostra também as do corretor, mas o envio é recusado.

---

## Banco de questões

Acervo de questões de múltipla escolha usado pelos quizzes e pelos simulados. A carga das provas de vestibular está descrita em [Arquitetura — Carga do banco de questões](arquitetura.md#carga-do-banco-de-questoes).

### Consulta

**Acesso:** com conta · **Onde:** Área do Professor → "Banco de Questões"; também na montagem de [simulado de treino](#montar-simulado-de-treino)

Busca por título ou enunciado, em páginas de 20 questões. Cada questão mostra título, dificuldade, banca, ano, número e texto base; as alternativas aparecem ao expandir a questão, sem indicar a correta.

### Cadastro de questões

**Acesso:** `create_question` · **Onde:** Área do Professor → "Nova Questão" · **Flag:** `mocktests_create_questions`

- Só há questões de **múltipla escolha**, com alternativas de A a E e a correta marcada.
- Campos obrigatórios: título, disciplina, assunto, tópico, banca, ano, número e enunciado. Opcionais: dificuldade, que começa em "Fácil", e texto de apoio.
- A disciplina, o assunto e o tópico são **digitados**: um nome que ainda não existe cria um novo ramo da taxonomia.
- O formulário não aceita imagens.

### Edição de questões

**Acesso:** `edit_question` · **Onde:** Painel Administrativo → "Moderação de Questões" → "Editar questão"

- Pela interface, permite alterar os dados da questão, o texto das alternativas existentes, o gabarito e o vínculo principal com a taxonomia. Pela tela, não é possível incluir ou remover alternativas nem trocar imagens.
- A edição exige ao menos duas alternativas, com letras distintas, e **exatamente uma correta**.
- Na interface, a edição fica no Painel Administrativo, que exige a permissão de administrador.
- Não há exclusão de questões.

### Denúncia de erro

**Acesso:** com conta · **Onde:** botão "Sinalizar", durante o quiz e na resolução de simulado

- O estudante escolhe o motivo — erro no enunciado, gabarito incorreto, alternativas duplicadas, imagem ilegível ou ausente, ou outro problema — e pode acrescentar detalhes, com até 2.000 caracteres.
- A denúncia entra na [moderação](#moderacao-de-questoes) como pendente. Não há limite de denúncias, e o estudante não acompanha o andamento das que fez.
- A Pergunta do Dia, a revisão do quiz e o banco de questões não têm o botão.

---

## Área do Professor

**Acesso:** qualquer uma das permissões de conteúdo ou de redação · **Onde:** aba "Professor" do cabeçalho (`/area_professor`)

Reúne três abas: **Banco de Questões**, com a consulta e o cadastro; **Propostas de Redação**, com a lista, a criação, a edição e a exclusão; e **Fila de Correção**, com o acesso à fila.

- Os botões de cadastro aparecem para todos que têm acesso à área; a permissão específica é conferida no envio.
- As permissões de simulados, `create_mocktest` e `manage_mocktests`, também dão acesso à área, que não tem ferramentas de simulados.
- Sem nenhuma das permissões, a área mostra o aviso "Acesso Restrito".

---

## Painel Administrativo

**Acesso:** `admin_permission` · **Onde:** aba "Admin" do cabeçalho (`/admin`) · **Flag:** `module_admin`, verificada só na interface

### Visão geral

- **Indicadores** — usuários cadastrados, com os novos dos últimos 7 dias; questões no banco; simulados, contando os de treino; questões sinalizadas, que é o número de denúncias pendentes; e permissões concedidas.
- **Modificações dos últimos 30 dias** — total de modificações registradas, sem contar as denúncias de estudantes; administradores que fizeram alguma modificação no período; questões adicionadas e removidas; e a última modificação.
- **Avisos**, como denúncias aguardando moderação e banco sem questões; as **cinco atualizações mais recentes** do registro de auditoria; e o pódio do **ranking geral** do IFQuiz.

### Usuários e permissões

- Busca por e-mail, apelido ou nome de permissão, em páginas de 20 usuários.
- Cada usuário mostra pontos, sequência e permissões. O administrador **concede** uma permissão escolhendo-a no catálogo e **revoga** clicando no "×" da permissão, sem pedido de confirmação.
- A permissão de administrador do administrador inicial não pode ser revogada.

### Moderação de questões

- Lista as denúncias filtradas por situação: pendentes, que é o padrão, resolvidas, descartadas ou todas.
- Cada denúncia pendente pode ser marcada como **resolvida** ou **descartada**. A questão denunciada pode ser **editada** ali mesmo, qualquer que seja a situação da denúncia, com a opção de resolver de uma vez todas as denúncias pendentes dela.

### Módulos

Liga e desliga cada *feature flag*. Com um módulo desligado, os interruptores das suas funcionalidades ficam desabilitados. O botão "Reset", que devolve a flag ao valor padrão, aparece apenas nas flags alteradas pelo painel.

### Registro de auditoria

São registrados o cadastro, a edição e a denúncia de questões, as mudanças de situação das denúncias, a criação, a edição e a exclusão de propostas de redação, a concessão e a revogação de permissões e as alterações das flags. Correções de redação, simulados e compras na loja não são registrados.

O painel mostra o resumo dos últimos 30 dias e as cinco atualizações mais recentes; não há consulta ao registro completo.

---

## Comportamentos comuns

### Sessão

A interface não exige login para abrir as telas internas, mas os dados só carregam para quem entrou: sem sessão, a API recusa as chamadas, e as telas aparecem com zeros ou listas vazias. Funcionam sem conta apenas os [temas de redação](#temas-de-redacao) e a consulta à situação dos módulos.

As abas "Professor" e "Admin" do cabeçalho aparecem depois que a plataforma carrega as permissões do usuário.

### Módulos desligados

| Situação | O que o usuário vê |
|---|---|
| Módulo desligado | O link do cabeçalho fica riscado e sem clique, o cartão da página Início fica cinza com o selo "Temporariamente desabilitado", e o endereço do módulo mostra a página "Em Breve" |
| Pergunta do Dia, Ranking ou Correção desligados | A tela da funcionalidade é substituída pela página "Em Breve" |
| Demais funcionalidades desligadas — quiz personalizado, loja, propostas, simulado aleatório e cadastro de questões | A tela continua disponível, mas o conteúdo não carrega ou a ação é recusada. Em parte das telas, a mensagem informa que o módulo está desativado e que um administrador pode reativá-lo no painel; em outras, aparece um erro genérico ou uma lista vazia |
| Exportação em PDF desligada | Nenhum efeito, porque a interface monta o caderno sem usar a exportação da API |
| Falha ao consultar os módulos | A interface não presume que estão ligados e mostra "Não foi possível verificar quais módulos estão ativos", com a opção de tentar de novo |

A regra de cada flag está em [Arquitetura — Feature flags](arquitetura.md#feature-flags).

### Falta de permissão

Quando falta uma permissão, a **API** recusa a ação e informa qual permissão está faltando: *"Você não tem a permissão '…' para concluir esta ação. Se você acha que isso é um erro, contate um administrador para solicitar a permissão."*

Na **interface**, a Área do Professor e o Painel Administrativo mostram a quem não tem acesso o aviso "Acesso Restrito", com o texto "Esta área é exclusiva para professores e administradores do IFVest.". Nas demais telas, o retorno varia: algumas exibem a mensagem da API, outras um erro genérico ou uma lista vazia.

### Datas e horários

A Pergunta do Dia, a sequência diária e o ranking semanal seguem o **horário de Brasília**.

---

## Previstas ou desativadas

| Item | Situação |
|---|---|
| Flashcards | Módulo previsto. A tela mostra "Em Breve" mesmo com a flag ligada, e não há rotas na API |
| Revisão de Conteúdo | Módulo previsto. A tela mostra "Em Breve" mesmo com a flag ligada, e não há rotas na API |
| Modo Competição do IFQuiz | Aparece na página do IFQuiz como "Em breve", desabilitado |
| Envio de redação por arquivo | Aba "Enviar arquivo (Em breve)", desabilitada: a extração do texto por OCR não faz parte da primeira versão |
| Simulados montados por professores | Rota na API, sem tela na interface |

O que foi definido para os módulos previstos está na [Descrição do Sistema](descricao-do-sistema.md#modulos).

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Regras de negócio, acesso e flags de cada funcionalidade | Código do backend do `ifvest-monorepo` (`src/api/v1/`, `src/services/` e `src/core/`) | out/2026 |
| Telas, ações, mensagens e condições de exibição | Código do frontend do `ifvest-monorepo` (`src/router/`, `src/features/` e `src/core/`) | out/2026 |
| Pontos, patentes, ranking e loja | `src/services/quiz_scoring.py`, `quiz_ranking.py`, `store_catalog.py` e `src/core/clock.py` | out/2026 |
| Critério do ranking e da patente | `docs/auditoria-testes-2026-09-25.md`, seção 12 | set/2026 |
| Seletor de dificuldade oculto | `docs/decisoes/0001-ocultar-seletor-de-dificuldade-do-quiz.md` | set/2026 |

!!! note "Divergências entre o README do backend e o código"
    A visão de negócio do README do backend descreve alguns comportamentos de forma diferente do que o código implementa — o login por e-mail e senha, a regra da sequência diária e o histórico de simulados, entre outros. Esta página adota o código. A lista completa está em [Descrição do Sistema — Fontes desta página](descricao-do-sistema.md#fontes-desta-pagina).
