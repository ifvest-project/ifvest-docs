# Requisitos Funcionais

Esta página registra o que o IFVest deve fazer, em dois níveis:

- **[Requisitos da plataforma](#requisitos-da-plataforma)** — o que a plataforma deve oferecer como um todo, da conta do usuário à administração. Partem da versão anterior desta especificação, atualizada para o IFVest V3 e complementada com as definições da equipe de desenvolvimento.
- **[Requisitos por módulo](#requisitos-por-modulo)** — o detalhamento de cada módulo, especificado pela equipe responsável por ele no levantamento de funcionalidades. Cada módulo indica os requisitos da plataforma que detalha.

Ao lado de cada requisito, a página indica a situação na versão em produção, conferida no código.

---

## Como ler esta página

- **ID** — os requisitos da plataforma são identificados por `RFG`, de *requisito funcional geral*. Os requisitos por módulo mantêm o identificador dado pela equipe no levantamento; como cada módulo tem a própria numeração, eles são citados com o nome do módulo, como em "RF6 do IFQuiz".
- **Situação no V3** — se a plataforma em produção já atende ao requisito:

| Situação | Significado |
|---|---|
| ✅ Atendido | A plataforma faz o que o requisito pede |
| 🟡 Em parte | A plataforma atende parte do requisito ou o atende de forma diferente; a observação explica |
| ⬜ Não atendido | Ainda não implementado |

- **Critérios de aceitação** — nos requisitos por módulo, reproduzidos do levantamento em blocos que se abrem com um clique. Eles orientam os testes e ainda não foram verificados um a um.

A especificação anterior e o levantamento descrevem os usuários como **aluno**, **professor** e **administrador**. No V3, o que cada usuário pode fazer depende das [permissões](../descricao-do-sistema.md#perfis-e-permissoes) que possui, e não de um perfil fixo; quando um requisito atendido cita um perfil, a observação indica a permissão correspondente.

---

## Requisitos da plataforma

Quinze requisitos vêm da especificação anterior, que os organizava por perfil de usuário; a numeração antiga está em [Correspondência com a especificação anterior](#correspondencia-com-a-especificacao-anterior). Os demais vêm das definições da equipe de desenvolvimento do V3: a visão de negócio do README do backend e as regras do projeto, no guia de contribuição do monorepo.

### Conta e acesso

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| <span id="rfg01">RFG01</span> | **Cadastro e entrada.** O usuário deve poder se cadastrar e entrar na plataforma com o e-mail institucional ou com a conta Google, por meio do Firebase Authentication. | 🟡 Em parte | A entrada é feita só pela conta Google — o que inclui os e-mails institucionais que sejam contas Google —, e não há cadastro com e-mail e senha. A conta é criada no primeiro acesso. |
| <span id="rfg02">RFG02</span> | **Recuperação de senha.** O sistema deve oferecer a recuperação de senha em três etapas: informar o e-mail, validar um código e definir a nova senha. | ⬜ Não atendido | Como não há cadastro com e-mail e senha, não há senha a recuperar na plataforma: a senha da conta Google é gerenciada pelo próprio Google. O requisito depende da entrada por e-mail prevista no [RFG01](#rfg01). |
| <span id="rfg03">RFG03</span> | **Gestão do perfil.** O usuário deve poder alterar a foto de perfil, atualizar os dados cadastrais e solicitar a exclusão da conta, conforme a LGPD. | 🟡 Em parte | É possível editar o apelido, que é o nome exibido no ranking. Não há foto de perfil nem exclusão de conta. |

### Permissões

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| <span id="rfg04">RFG04</span> | **Permissões individuais.** O que cada usuário pode fazer deve depender de permissões individuais, e não de perfis fixos. Os administradores concedem e revogam as permissões, escolhidas num catálogo único. | ✅ Atendido | O catálogo tem sete permissões, geridas no Painel Administrativo. Ver [Descrição do Sistema — Perfis e permissões](../descricao-do-sistema.md#perfis-e-permissoes). |
| <span id="rfg05">RFG05</span> | **Permissões iniciais.** As contas com e-mail institucional docente (`@ifsp.edu.br`) devem receber automaticamente as permissões docentes, e a conta do administrador inicial, definida na configuração do servidor, as de administrador. As permissões iniciais são atribuídas só na criação da conta, para que as mudanças feitas depois pelos administradores se mantenham. | ✅ Atendido | As permissões docentes são as de cadastro e edição de questões, de criação de simulados institucionais e de gestão dos simulados de outras pessoas. Ver [Como as permissões são atribuídas](../descricao-do-sistema.md#como-as-permissoes-sao-atribuidas). |
| <span id="rfg06">RFG06</span> | **Aviso de permissão.** Quando o usuário tentar uma ação sem a permissão necessária, o sistema deve informar qual permissão falta e orientá-lo a pedi-la a um administrador. | 🟡 Em parte | A API responde com essa mensagem. Na interface, parte das telas a exibe, e outras mostram um erro genérico ou uma lista vazia. Ver [Falta de permissão](../funcionalidades.md#falta-de-permissao). |

### Conteúdo e banco de questões

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| <span id="rfg07">RFG07</span> | **Organização do conteúdo.** O conteúdo deve seguir a hierarquia Disciplina → Assunto → Tópico. Cada questão se vincula a um ou mais tópicos, dos quais herda o assunto e a disciplina. | ✅ Atendido | Ver [Descrição do Sistema — Organização do conhecimento](../descricao-do-sistema.md#organizacao-do-conhecimento). |
| <span id="rfg08">RFG08</span> | **Gestão de questões.** O professor deve poder criar questões manualmente ou importá-las de um banco de questões existente, por meio de APIs do ENEM e da FUVEST. | 🟡 Em parte | O cadastro e a edição existem, com as permissões `create_question` e `edit_question`. A importação em lote existe, mas a partir de arquivos, e não de APIs: pela carga no servidor ou por um `.zip` enviado no Painel Administrativo, restrito aos administradores. |
| <span id="rfg09">RFG09</span> | **Atualização do banco de questões.** O sistema deve consumir APIs externas para manter o banco de questões atualizado com as provas mais recentes do ENEM e da FUVEST. | ⬜ Não atendido | As provas entram por carga ou importação de arquivos, descritas em [Arquitetura — Carga do banco de questões](../arquitetura.md#carga-do-banco-de-questoes). |
| <span id="rfg10">RFG10</span> | **Qualidade do conteúdo.** Administradores e moderadores devem zelar pela qualidade pedagógica do conteúdo, auditando o que é publicado na plataforma. | 🟡 Em parte | Os usuários denunciam erros nas questões, e os administradores moderam as denúncias e corrigem as questões no Painel Administrativo. As alterações de conteúdo ficam no registro de auditoria, inclusive as feitas pela carga e pela importação de questões, mas o painel mostra só o resumo dos últimos 30 dias e as cinco alterações mais recentes. |

### Estudo e prática

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| <span id="rfg11">RFG11</span> | **Revisão de Conteúdo.** O estudante deve acessar materiais de estudo organizados pela hierarquia de conteúdo, com um material por tópico. | ⬜ Não atendido | Módulo previsto, sem implementação. A especificação anterior dividia os materiais por áreas (Matemática, Humanas, Naturais, Linguagens e Informática); a definição do V3 os organiza por tópico. Ver [Descrição do Sistema — Revisão de Conteúdo](../descricao-do-sistema.md#revisao-de-conteudo). |
| <span id="rfg12">RFG12</span> | **Formatos dos materiais.** O sistema deve exibir videoaulas, textos teóricos em Markdown e exercícios de fixação para cada tópico. | ⬜ Não atendido | Depende do módulo de Revisão de Conteúdo. |
| <span id="rfg13">RFG13</span> | **Autoria dos materiais.** O professor deve poder criar e editar os materiais de revisão num editor Markdown com pré-visualização em tempo real. A autoria é colaborativa, com histórico das alterações, e cada edição entra no ar na hora, marcada como pendente de auditoria até ser revisada por um administrador. | ⬜ Não atendido | Depende do módulo de Revisão de Conteúdo. A autoria colaborativa, o histórico e a auditoria pendente vêm da definição do V3. |
| <span id="rfg14">RFG14</span> | **Flashcards.** O estudante deve poder estudar com flashcards, criando os próprios baralhos ou usando baralhos institucionais criados por professores. | ⬜ Não atendido | Módulo previsto, sem implementação. A definição do V3 prevê baralhos públicos e privados, a importação de baralhos públicos por referência e o agendamento das revisões por repetição espaçada. Ver [Descrição do Sistema — Flashcards](../descricao-do-sistema.md#flashcards). |
| <span id="rfg15">RFG15</span> | **Baralhos oficiais.** O professor deve poder criar e disponibilizar baralhos oficiais de flashcards para os estudantes. | ⬜ Não atendido | Depende do módulo de Flashcards. |
| <span id="rfg16">RFG16</span> | **IFQuiz.** O estudante deve poder fazer quizzes filtrados por disciplina, assunto e etiquetas, acompanhando seu placar e desempenho. | 🟡 Em parte | Os quizzes filtram por disciplina e assunto; as questões não têm etiquetas. O módulo tem também Pergunta do Dia, sequência diária, pontos, patentes, ranking e loja de avatares, detalhados nos [requisitos do IFQuiz](#ifquiz). |
| <span id="rfg17">RFG17</span> | **Simulados.** O estudante deve poder montar simulados com questões escolhidas uma a uma ou geradas por filtros da hierarquia de conteúdo, e o sistema deve registrar o histórico das tentativas, com o tempo gasto, as respostas dadas e a pontuação. | 🟡 Em parte | Os simulados são montados por seleção, com filtros de disciplina, assunto, banca e ano, ou por sorteio, que na interface só filtra por disciplina. Cada tentativa registra os acertos, a nota e a resposta dada em cada questão, mas não o tempo gasto. O histórico das tentativas fica no Perfil. |
| <span id="rfg18">RFG18</span> | **Recomendação de estudo.** O sistema deve sugerir materiais e exercícios com base no histórico de desempenho e nos erros do estudante. | ⬜ Não atendido | Objeto do subprojeto [Sistemas de Recomendação aplicados à IFVest](../subprojetos/ia-e-recomendacao.md#sistemas-de-recomendacao-aplicados-a-ifvest). |

### Redação

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| <span id="rfg19">RFG19</span> | **Propostas de redação.** O professor deve poder publicar propostas temáticas de redação, com textos motivadores e imagens. | ✅ Atendido | Com a permissão `create_essay_proposal_permission`. As regras das propostas estão nos [requisitos da Redação](#redacao). |
| <span id="rfg20">RFG20</span> | **Envio de redação.** O estudante deve poder enviar redações, manuscritas ou digitadas, para correção automatizada ou por professores. | 🟡 Em parte | Só redações digitadas na própria plataforma, corrigidas por corretores. O envio por imagem e a correção automatizada dependem do [RFG22](#rfg22). |
| <span id="rfg21">RFG21</span> | **Correção de redação.** O corretor deve poder ver as redações enviadas e corrigi-las pela grade de competências do ENEM (C1 a C5), com devolutiva descritiva, complementando a correção automatizada. | ✅ Atendido | Com a permissão `grade_essay_permission`, incluindo comentários em trechos do texto. A correção automatizada, que ela complementaria, ainda não existe. |
| <span id="rfg22">RFG22</span> | **Correção por OCR e IA.** O sistema deve reconhecer o texto de redações manuscritas por OCR e sugerir correções com base em redes neurais. | ⬜ Não atendido | Em desenvolvimento num subprojeto à parte, ainda não integrado à plataforma: ver [Envio de redação por imagem e OCR](#envio-de-redacao-por-imagem-e-ocr). |

### Administração e regras gerais

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| <span id="rfg23">RFG23</span> | **Controle dos módulos.** Os administradores devem poder ligar e desligar módulos e funcionalidades sem alterar o código. Com um módulo desligado, a API deve recusar as chamadas a ele, e a interface deve explicar ao usuário que o módulo está indisponível. | 🟡 Em parte | O controle fica no Painel Administrativo, e a API recusa as chamadas aos módulos desligados — exceto ao próprio painel, cuja flag é verificada só na interface. Parte das telas explica que o módulo está desligado; outras mostram um erro genérico ou uma lista vazia. Ver [Módulos desligados](../funcionalidades.md#modulos-desligados). |
| <span id="rfg24">RFG24</span> | **Horário de referência.** As funcionalidades que dependem do dia ou da semana — Pergunta do Dia, sequência diária e ranking semanal — devem seguir o horário de Brasília. | ✅ Atendido | O servidor grava as datas em UTC e calcula o dia e a semana no horário de Brasília. |

⬜ *Sem requisito correspondente: os simulados institucionais, o caderno e o gabarito dos simulados e os indicadores do Painel Administrativo existem na plataforma, mas não constam das fontes desta especificação. Os requisitos deles devem vir do levantamento, quando os simulados e a administração forem preenchidos.*

---

## Requisitos por módulo

Os requisitos por módulo vêm do **Levantamento de Funcionalidades e Regras de Negócio**, documento compartilhado em que cada equipe descreve as funcionalidades sob sua responsabilidade: objetivo, regras de negócio, fluxos, critérios de aceitação e riscos.

!!! info "Levantamento em andamento"
    O levantamento está sendo preenchido ao longo do tempo, e esta seção acompanha o seu avanço. Versão usada nesta página: **20/10/2026**.

| Módulo | Responsável no levantamento | Situação do levantamento | Detalha |
|---|---|---|---|
| [IFQuiz](#ifquiz) | Helena Vieira Nascimento | ✅ Preenchido — nove funcionalidades | [RFG16](#rfg16) |
| [Redação](#redacao) | Guilherme Augusto Frazão Ribeiro | 🟡 Preenchido para o módulo como um todo, sem numeração dos requisitos | [RFG19](#rfg19) a [RFG21](#rfg21) |
| [Redação — envio por imagem e OCR](#envio-de-redacao-por-imagem-e-ocr) | Arthur Araújo de Oliveira | ✅ Preenchido | [RFG20](#rfg20) e [RFG22](#rfg22) |
| Autenticação, login e cadastro | Wilker | ⬜ Aguardando preenchimento | [RFG01](#rfg01) a [RFG03](#rfg03) |
| Simulados | — | ⬜ Aguardando preenchimento | [RFG17](#rfg17) |
| Flashcards | — | ⬜ Aguardando preenchimento | [RFG14](#rfg14) e [RFG15](#rfg15) |
| Revisão de Conteúdo | — | ⬜ Aguardando preenchimento | [RFG11](#rfg11) a [RFG13](#rfg13) |
| [IFVest Reader](../subprojetos/ifvest-reader.md) | João Paulo | ⬜ Aguardando preenchimento | — *(aplicativo à parte)* |

O banco de questões e a administração — permissões, moderação de denúncias e controle dos módulos — ainda não têm seção no levantamento. Por enquanto, estão cobertos apenas pelos requisitos da plataforma: de [RFG04](#rfg04) a [RFG10](#rfg10) e o [RFG23](#rfg23).

### IFQuiz

Requisitos especificados por **Helena Vieira Nascimento**, nas entradas #001 a #009 do levantamento, que detalham o [RFG16](#rfg16). O que o módulo faz hoje está em [Descrição das Funcionalidades — IFQuiz](../funcionalidades.md#ifquiz).

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| RF1 | O sistema deve permitir que o usuário inicie um novo jogo e escolha os tópicos que quer responder. | ✅ Atendido | A escolha é feita por disciplina e assunto. |
| RF2 | O sistema deve permitir filtrar as perguntas por disciplina, assunto, dificuldade (Fácil, Média ou Difícil) e quantidade de questões. | 🟡 Em parte | Não há filtro de dificuldade: o seletor foi ocultado por decisão da equipe, porque a dificuldade registrada nas questões ainda não reflete a real. |
| RF3 | O jogo deve exibir perguntas e respostas de acordo com o tema escolhido. | ✅ Atendido | |
| RF4 | Após cada resposta, o sistema deve destacar a alternativa correta e a escolhida, quando errada, como retorno imediato. | ✅ Atendido | |
| RF5 | O sistema deve disponibilizar diariamente uma questão única e igual para todos os usuários, com uma tentativa por dia; recompensar o acerto com pontos; e exibir estatísticas comparativas, como o percentual de acertos da comunidade e o total de respostas. | ✅ Atendido | O acerto vale 100 pontos, e não os 20 do RF7. |
| RF6 | O sistema deve permitir partidas competitivas em tempo real entre dois usuários, com limite de 3 minutos por questão, pontos para o jogador com melhor desempenho e registro do resultado no histórico. | ⬜ Não atendido | Fora da primeira versão, como registra o próprio levantamento. A página do IFQuiz mostra o modo como "Em breve". |
| RF7 | O sistema deve atribuir e exibir pontos a cada questão respondida corretamente; hoje, 20 pontos por acerto. | 🟡 Em parte | Os 20 pontos por acerto aparecem durante a partida, mas são somados ao saldo só ao fim do quiz, e não a cada resposta. |
| RF8 | O sistema deve manter uma sequência diária (*streak*): iniciada no primeiro login, incrementada a cada dia em que o usuário entra e responde perguntas, com pontos a cada incremento, e zerada se ele não entrar no dia. | 🟡 Em parte | A plataforma conta os dias seguidos com resposta à Pergunta do Dia, como descreve a entrada #003 do levantamento; entrar na plataforma não conta, e a sequência não rende pontos. As entradas #003 e #005 descrevem a regra de formas diferentes. |
| RF9a | O sistema deve ter exatamente sete patentes, definidas pela pontuação — Bronze (0 a 499), Prata (500 a 999), Ouro (1.000 a 1.999), Platina (2.000 a 3.499), Diamante (3.500 a 4.999), Mestre (5.000 a 7.499) e Lenda do IF (7.500 ou mais) —, promovendo ou rebaixando o usuário conforme a pontuação varia. | ✅ Atendido | A patente acompanha o saldo de pontos, que também diminui com as compras na loja. |
| RF9b | A cada patente atingida, o sistema deve conceder automaticamente itens exclusivos de personalização do avatar. | ⬜ Não atendido | Os avatares disponíveis são todos comprados com pontos na loja. |
| RF10 | O sistema deve manter e atualizar um ranking de usuários com base na patente atual (RF9a) e no tamanho da sequência (RF8), com desempate pela sequência e pela antiguidade do cadastro e com a opção de carregar mais posições. | 🟡 Em parte | O ranking ordena pelos pontos ganhos, num período geral e num semanal, e exibe a patente e a sequência de cada usuário. Empates dividem a mesma posição, e a interface mostra os dez primeiros colocados. |
| RF11 | O sistema deve permitir que o usuário crie e personalize um avatar, e oferecer uma loja em que ele usa os pontos acumulados para adquirir itens de personalização; a personalização inclui os itens comprados e os concedidos por patente. | 🟡 Em parte | Há a loja e a troca de avatar, mas cada avatar é um item único, sem personalização por partes, e não há itens de patente (RF9b). |
| RF12 | O sistema deve armazenar e exibir o histórico de resultados de cada jogador: as partidas da prática livre, com opção de refazer; a Pergunta do Dia, com gráfico de acertos, erros e dias sem resposta; e o modo competição, com vitórias, derrotas e desempenho. | 🟡 Em parte | O Perfil mostra o histórico da prática livre, com a opção *Refazer*, e o mapa de calor da Pergunta do Dia. O histórico do modo competição depende do RF6. |

??? note "Critérios de aceitação — #001 Prática Livre"
    - Os filtros de disciplina e assunto devem carregar dinamicamente as opções válidas.
    - A partida só deve iniciar se houver perguntas cadastradas suficientes para o filtro aplicado.
    - O layout das perguntas deve exibir enunciado e alternativas de forma clara e responsiva.

??? note "Critérios de aceitação — #002 Validação de respostas e pontuação"
    - Feedback visual de acerto ou erro perceptível em menos de 2 segundos.
    - Atualização imediata do contador de pontuação exibido na interface.
    - Impossibilidade de alterar a alternativa selecionada após a confirmação.

??? note "Critérios de aceitação — #003 Pergunta do Dia"
    - Bloqueio estrito de mais de uma resposta diária por usuário.
    - Exibição precisa do percentual de acertos coletivo da comunidade.
    - Registro da tentativa no histórico do usuário, para exibição no calendário anual.

??? note "Critérios de aceitação — #004 Modo Competição"
    - Cronômetro decrescente visível e travamento da resposta ao esgotar os 3 minutos.
    - Sincronização entre os dois competidores com latência menor que 2 segundos (RNF1).
    - Registro do resultado no histórico do perfil (RF12).

??? note "Critérios de aceitação — #005 Sequência diária"
    - Exibição do contador de dias de sequência na página inicial, no ranking e no perfil.
    - Reinício automático da sequência ao virar o dia sem registro de atividade.
    - Registro histórico da evolução da sequência.

??? note "Critérios de aceitação — #006 Patentes e itens exclusivos"
    - O cartão de patente deve exibir o intervalo correto e quantos pontos faltam para o próximo nível.
    - A identificação visual da patente, com nome e ícone, deve estar sincronizada em toda a plataforma.
    - Liberação imediata dos itens de patente no inventário do usuário.

??? note "Critérios de aceitação — #007 Ranking"
    - Ordenação fiel, respeitando patente, pontuação e sequência.
    - Posição do próprio jogador sempre destacada, para rápida identificação.
    - Tempo de resposta do ranking inferior a 2 segundos (RNF1).

??? note "Critérios de aceitação — #008 Avatares e loja"
    - Débito correto e imediato do saldo de pontos ao comprar um item.
    - Itens de patente (RF9b) não podem ser vendidos por pontos, apenas desbloqueados por mérito.
    - O avatar atualizado deve ser visível para os outros competidores e no ranking.

??? note "Critérios de aceitação — #009 Histórico"
    - Histórico exibindo acertos, pontos ganhos e datas com precisão.
    - Clique nas células do calendário da Pergunta do Dia levando ao feedback da data correspondente.
    - Gravação imediata de cada partida finalizada no banco de dados (RNF6).

### Redação

Regras especificadas por **Guilherme Augusto Frazão Ribeiro** para o módulo como um todo, que detalham os requisitos [RFG19](#rfg19) a [RFG21](#rfg21). O que o módulo faz hoje está em [Descrição das Funcionalidades — Redação](../funcionalidades.md#redacao).

| Tema | Regra | Situação no V3 | Observação |
|---|---|---|---|
| Escrita | Todo usuário pode escrever redações sobre as propostas disponíveis. | ✅ Atendido | |
| Exclusão de redações | Todo usuário pode apagar as redações que escreveu. | ⬜ Não atendido | Não há exclusão de redações. |
| Papéis | Professores podem criar propostas e corrigir redações. | ✅ Atendido | No V3, pelas permissões `create_essay_proposal_permission` e `grade_essay_permission`. |
| Edição de propostas | Apenas o professor que criou uma proposta pode editá-la ou removê-la, junto com seus textos motivadores. | 🟡 Em parte | O administrador também pode. |
| Textos motivadores | Toda proposta deve ter ao menos um texto motivador. | ⬜ Não atendido | É possível criar propostas sem textos de apoio. |
| Tamanho mínimo | Toda redação deve ter ao menos 7 linhas, aproximadamente; com menos, o envio é bloqueado e o sistema informa o mínimo de linhas. | 🟡 Em parte | O envio exige ao menos 10 caracteres. O editor mostra a estimativa de linhas, mas não a usa como limite. |
| Comentários na correção | Toda correção deve ter ao menos um comentário, contando o parecer geral. | ✅ Atendido | A tela de correção exige o parecer geral. |
| Corretor ou IA | A correção pode ser feita por um corretor ou por IA. | 🟡 Em parte | Só por corretor. A correção por IA depende do [subprojeto de OCR e IA](#envio-de-redacao-por-imagem-e-ocr). |
| Rascunho | O rascunho da redação fica salvo por até 10 minutos e é descartado depois. | ✅ Atendido | O rascunho é salvo no navegador. |

⬜ *Numerar as regras com a equipe: o levantamento não as numera, mas o código da plataforma se refere à regra do rascunho como RF17 e à gestão das propostas como RF9, o que indica uma numeração já em uso.*

??? note "Critérios de aceitação — Redação"
    - Professores conseguem criar, editar e remover propostas de redação e seus textos motivadores, conforme as regras de negócio.
    - As propostas de redação são exibidas corretamente e podem ser acessadas pelos usuários.
    - Os usuários conseguem solicitar a correção das suas redações, desde que sigam as regras de negócio.

### Envio de redação por imagem e OCR

Requisitos especificados por **Arthur Araújo de Oliveira**, para o subprojeto que permite enviar a foto de uma redação manuscrita e extrair o texto para a correção automática por IA, com base em critérios de vestibulares como o ENEM e a FUVEST. Detalham o envio por imagem previsto no [RFG20](#rfg20) e a correção por OCR e IA do [RFG22](#rfg22).

O subprojeto tem backend próprio, em Python com Flask, e **ainda não está integrado à plataforma**: no V3, a opção de enviar a redação por arquivo aparece como "Em breve", e nenhuma das regras abaixo é atendida ainda.

- O sistema deve aceitar imagens de redações manuscritas, nos formatos permitidos pela aplicação.
- O texto digitado deve ser recebido sem passar pelo reconhecimento por OCR.
- Para imagens, o sistema deve usar OCR ou um modelo multimodal para extrair o texto.
- O conteúdo extraído deve seguir para a etapa de análise e correção.
- O sistema deve informar o usuário quando não conseguir processar a imagem ou extrair o texto adequadamente.
- O texto reconhecido deve preservar, sempre que possível, as palavras e a estrutura originais da redação.

??? note "Critérios de aceitação — Envio por imagem e OCR"
    - O sistema permite enviar uma redação manuscrita por imagem e inserir um texto digitado.
    - O texto extraído representa o conteúdo original com a maior fidelidade possível.
    - O conteúdo processado é disponibilizado para a etapa de correção automática.
    - Entradas inválidas, imagens ilegíveis e falhas de processamento geram mensagens claras.
    - O processamento é testado com diferentes tipos de escrita e condições de imagem.

---

## Correspondência com a especificação anterior

A versão anterior desta página, escrita antes do IFVest V3, organizava os requisitos por perfil de usuário — estudante e professor ou administrador — e por módulos de inteligência e integração, de RF01 a RF15. Todos foram mantidos nos requisitos da plataforma, atualizados para o V3:

| Anterior | Requisito | Nesta versão |
|---|---|---|
| RF01 | Autenticação segura | [RFG01](#rfg01) |
| RF02 | Recuperação de senha | [RFG02](#rfg02) |
| RF03 | Gestão de perfil | [RFG03](#rfg03) |
| RF04 | Revisão de conteúdo | [RFG11](#rfg11) |
| RF05 | Consumo de materiais | [RFG12](#rfg12) |
| RF06 | Prática com IFQuiz | [RFG16](#rfg16) |
| RF07 | Uso de flashcards | [RFG14](#rfg14) |
| RF08 | Submissão de redação | [RFG20](#rfg20) |
| RF09 | Criação de conteúdo | [RFG13](#rfg13) |
| RF10 | Gestão de exercícios | [RFG08](#rfg08) |
| RF11 | Curadoria de flashcards | [RFG15](#rfg15) |
| RF12 | Correção de redações | [RFG21](#rfg21) |
| RF13 | Correção via OCR e IA | [RFG22](#rfg22) |
| RF14 | Recomendação de estudo | [RFG18](#rfg18) |
| RF15 | Integração de questões | [RFG09](#rfg09) |

Os requisitos de [RFG04](#rfg04) a [RFG07](#rfg07), o [RFG10](#rfg10), o [RFG17](#rfg17), o [RFG19](#rfg19), o [RFG23](#rfg23) e o [RFG24](#rfg24) foram acrescentados a partir das definições da equipe do V3. A página anterior está preservada no histórico do repositório, na etiqueta `legado-v2`.

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Requisitos da plataforma vindos da especificação anterior | Versão anterior desta página, preservada na etiqueta `legado-v2` | ago/2026 |
| Requisitos da plataforma acrescentados no V3 | Visão de negócio do `ifvest-backend/README.md` e regras do projeto em `docs/guia/06-regras-do-projeto.md`, no `ifvest-monorepo` | out/2026 |
| Requisitos por módulo, regras e critérios de aceitação | Levantamento de Funcionalidades e Regras de Negócio, preenchido pelas equipes de cada módulo | 20/10/2026 |
| Situação no V3 | Código do backend e do frontend do `ifvest-monorepo` (commit `d36de12`, de 15/10/2026), conforme a [Descrição das Funcionalidades](../funcionalidades.md) | out/2026 |
| Decisão sobre o filtro de dificuldade | `docs/decisoes/0001-ocultar-seletor-de-dificuldade-do-quiz.md`, no `ifvest-monorepo` | set/2026 |
