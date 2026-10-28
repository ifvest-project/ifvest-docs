# Banco de Questões

O **banco de questões** reúne as questões de múltipla escolha usadas nos quizzes do IFQuiz e nos simulados. Cada questão se vincula a um **tópico**, dentro de um assunto e de uma disciplina (ver [Como os conteúdos são organizados](../glossario.md#como-os-conteudos-sao-organizados)), e pode aparecer em quantos quizzes e simulados houver.

O acervo combina as **provas de vestibulares**, que entram em lote pela [importação](#tarefa-5-importar-questoes-em-lote), e as **questões autorais**, cadastradas uma a uma pelos professores.

---

## Tarefa 1 — Consultar o banco de questões

**Status:** ✅ Disponível  
**Acesso:** qualquer permissão de conteúdo ou de redação

**Objetivo:** encontrar questões do banco e conferir o seu conteúdo.

**Pré-requisitos:** ter entrado na plataforma com uma conta que tenha permissão de professor (ver [Permissões](index.md#para-quem-e-este-guia)).

**Como fazer:**

1. No cabeçalho, clique em **Professor**. A Área do Professor abre na aba **Banco de Questões**.
2. Busque no campo **Pesquisar por título ou enunciado...**. A lista vem em páginas de 20 questões.
3. Cada questão mostra o título, a disciplina, o assunto, a dificuldade, a banca, o ano e o número, além do enunciado e do texto base, quando houver. Para ver as alternativas, clique em **Ver Alternativas** — o número entre parênteses indica quantas são.

**Observações:**

- A lista mostra **todas as questões do banco**, e não só as cadastradas por você.
- A consulta não indica a alternativa correta.
- A busca com filtros de disciplina, assunto, banca e ano existe na [montagem de simulados](../aluno/simulados.md#tarefa-1-montar-um-simulado-de-treino), aberta a qualquer estudante.

---

## Tarefa 2 — Cadastrar uma questão

**Status:** ✅ Disponível  
**Acesso:** `create_question`

**Objetivo:** acrescentar ao banco uma questão autoral ou de uma prova que não veio pela importação.

**Pré-requisitos:** ter a permissão `create_question`.

**Como fazer:**

1. Na aba **Banco de Questões** da Área do Professor, clique em **+ Nova Questão**. O formulário **Nova Questão de Múltipla Escolha** se abre no lugar da lista.
2. Preencha os campos, na ordem em que aparecem:

    | Campo | Como preencher |
    |---|---|
    | **Título da Questão** | Obrigatório. Identifica a questão nas listas — por exemplo, "Questão 1 - Processo Seletivo 2024" |
    | **Disciplina**, **Matéria / Assunto** e **Tópico** | Obrigatórios. Digitados por você (ver aviso abaixo) |
    | **Banca / Instituição** | Obrigatório. Campo livre, que vem preenchido com IFSP |
    | **Ano** e **Número** | Obrigatórios. Vêm preenchidos com o ano atual e o número 1 |
    | **Dificuldade** | Fácil, Média ou Difícil; vem em Fácil |
    | **Texto de Apoio (Opcional)** | Texto base, citação ou contexto, exibido antes do enunciado |
    | **Enunciado da Questão** | Obrigatório |

3. Em **Alternativas (marque a opção correta)**, escreva o texto das alternativas de A a E e marque a correta.
4. Clique em **Cadastrar Questão**. A mensagem *"Questão "…" cadastrada com sucesso!"* confirma o cadastro, e a questão entra na lista.

Para desistir, clique em **Cancelar** ou em **Fechar Formulário**.

!!! warning "A disciplina, o assunto e o tópico são digitados"
    Não há uma lista para escolher: se o nome digitado ainda não existir, a plataforma cria um **novo ramo** na organização dos conteúdos. Um erro de digitação — "Matematica" em vez de "Matemática", por exemplo — cria uma disciplina duplicada. Antes de cadastrar, confira na [consulta](#tarefa-1-consultar-o-banco-de-questoes) como os nomes já aparecem nas questões existentes.

**Observações:**

- A alternativa **A** vem marcada como correta: confira a marcação antes de cadastrar.
- O formulário não aceita imagens. Questões com figuras entram pela [importação](#tarefa-5-importar-questoes-em-lote).
- O enunciado, o texto de apoio e as alternativas aceitam formatação **Markdown**, como listas, tabelas e negrito. Fórmulas em **LaTeX não são formatadas**: aparecem como texto.
- Não é possível excluir uma questão depois de cadastrada. Os erros são corrigidos pela [edição](#tarefa-3-editar-uma-questao).

---

## Tarefa 3 — Editar uma questão

**Status:** ✅ Disponível  
**Acesso:** `admin_permission` (ver aviso abaixo)

**Objetivo:** corrigir uma questão do banco — o enunciado, as alternativas, o gabarito ou a classificação.

**Pré-requisitos:** a questão ter ao menos uma denúncia de erro, pendente ou não.

!!! warning "A edição fica na moderação, no Painel Administrativo"
    A permissão `edit_question` autoriza a edição, mas a tela de edição só existe na **Moderação de Questões** do Painel Administrativo, a partir de uma denúncia, e o painel exige a permissão de administrador. Quem tem só `edit_question` não encontra onde editar.

    Para corrigir uma questão que ainda não tem denúncia, sinalize o erro durante um quiz ou um simulado (ver [Denunciar um erro numa questão](../aluno/simulados.md#tarefa-7-denunciar-um-erro-numa-questao)). A denúncia aparece na moderação, e dali um administrador edita a questão.

**Como fazer:**

1. No cabeçalho, clique em **Admin** e abra a aba **Moderação de Questões**.
2. Localize a denúncia da questão. A lista começa nas denúncias **Pendentes**; os botões **Resolvidas**, **Descartadas** e **Todas** mostram as demais.
3. Clique em **Editar questão**. O formulário **Editar Questão #…** se abre logo abaixo da denúncia, com os mesmos campos do cadastro, já preenchidos.
4. Altere o que for preciso: os dados da questão, o texto das alternativas, a alternativa correta e a classificação.
5. Se a questão tiver denúncias pendentes, o formulário traz, já marcada, a caixa que as marca como resolvidas ao salvar. Desmarque-a se quiser tratá-las depois.
6. Clique em **Salvar alterações**. A mensagem informa a questão atualizada e quantas denúncias foram resolvidas.

**Observações:**

- A edição exige ao menos duas alternativas, com letras diferentes, e **exatamente uma correta**.
- Pela tela, não é possível incluir ou remover alternativas nem trocar as imagens, que são mantidas como estão.
- Como no cadastro, a disciplina, o assunto e o tópico são digitados: um nome que ainda não existe cria um ramo novo.
- A edição vale para todos os quizzes e simulados que usam a questão: o vínculo é com a própria questão, e não com uma cópia.
- Uma questão corrigida na moderação fica protegida: uma importação posterior não desfaz a correção, a menos que o administrador peça para substituí-la.

---

## Tarefa 4 — Tratar as denúncias de erro

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** encerrar as denúncias feitas pelos estudantes, depois de conferir a questão.

**Pré-requisitos:** ter a permissão de administrador.

**Como fazer:**

1. No Painel Administrativo, abra a aba **Moderação de Questões**. Cada denúncia mostra o número da questão, o motivo escolhido pelo estudante e, quando houver, a descrição que ele escreveu.
2. Confira a questão. Se houver erro, corrija-a pela [Tarefa 3](#tarefa-3-editar-uma-questao), que pode resolver as denúncias ao salvar.
3. Para encerrar uma denúncia sem editar a questão, clique em **Marcar como Resolvida** ou, se não houver erro, em **Descartar**.

**Observações:**

- Na **Visão Geral** do painel, o indicador **Questões sinalizadas** mostra quantas denúncias estão pendentes, e o botão **Corrigir questões** leva à moderação.
- O estudante não é avisado de que a denúncia foi tratada.

---

## Tarefa 5 — Importar questões em lote

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** acrescentar ao banco as questões de uma ou mais provas de uma vez, ou corrigir as que já estão nele, a partir dos arquivos das provas.

**Pré-requisitos:** ter a permissão de administrador e os arquivos das provas, no formato em que saem da extração: uma pasta por prova, com um arquivo `.json` por questão e as figuras na pasta `imgs/` ou `imagens/`.

**Como fazer:**

1. Junte numa pasta as pastas das provas e compacte-a em `.zip`. No Windows: botão direito na pasta, **Enviar para**, **Pasta compactada**.
2. No Painel Administrativo, abra a aba **Importar Questões**.
3. Em **Arquivo .zip com as questões**, escolha o arquivo e confira as opções:

    | Opção | Padrão | O que faz |
    |---|---|---|
    | **Corrigir as questões que já estão no site** | Marcada | Atualiza com o conteúdo do zip as questões que já existem, identificadas pela banca, pelo ano, pelo número e pela prova. Desmarcada, só as questões novas entram |
    | **Substituir também as questões corrigidas à mão pela moderação** | Desmarcada | Aplica o zip também às questões editadas na moderação. Só pode ser marcada junto com a anterior. Deixe desmarcada para não desfazer essas correções |

4. Clique em **Enviar e simular**. A plataforma lê o zip e mostra o que **aconteceria**, sem gravar nada: quantas questões seriam inseridas e corrigidas, o que mudaria em cada uma, as que ficam de fora e por quê, as imagens que faltam e os arquivos que não puderam ser lidos. Em arquivos grandes, a simulação leva alguns minutos, e a tela se atualiza sozinha.
5. Se o relatório estiver como esperado, clique em **Aplicar importação**. A plataforma grava exatamente o que a simulação mostrou, e você pode sair da página enquanto ela roda.
6. Acompanhe o andamento no **Histórico**, que lista as importações com data, arquivo, tipo — simulação ou aplicação —, situação e quem enviou. **Ver relatório** reabre o relatório de cada uma.

**Observações:**

- **Limites:** 300 MB por arquivo, 1 GB descompactado e 50 mil arquivos. Acima disso, divida as provas em mais de um zip.
- Só entram questões completas: ao menos duas alternativas, todas com texto ou imagem, e exatamente uma correta. As demais aparecem no relatório, com o motivo, até que o arquivo seja corrigido.
- As questões discursivas do zip não entram: o banco tem só questões de múltipla escolha.
- Os textos compartilhados por várias questões viram o texto de apoio de cada uma.
- Para corrigir questões que já estão no banco, o zip pode ter só os arquivos corrigidos, na pasta da respectiva prova.
- Só uma importação roda por vez. O zip fica guardado por 24 horas; depois disso, ou se o servidor reiniciar, é preciso enviá-lo de novo para aplicar.
- A importação nunca remove questões.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A Área do Professor mostra **Acesso Restrito** | A sua conta não tem nenhuma permissão de conteúdo ou de redação. Peça-a a um administrador |
| *"Erro ao cadastrar a questão. Verifique os dados e tente novamente."* | Confira os campos e tente de novo. A mesma mensagem aparece quando a conta não tem a permissão `create_question` ou quando um administrador desligou o cadastro de questões em **Módulos (Feature Flags)** |
| Cadastrei uma questão e a disciplina apareceu duplicada | O nome foi digitado de forma diferente da existente. Um administrador pode corrigir a classificação da questão na moderação |
| A fórmula do enunciado aparece como texto | A plataforma não formata LaTeX. Escreva a fórmula em texto simples ou use uma imagem, pela importação |
| *"Aguarde a importação em andamento terminar para enviar outro arquivo."* | Só uma importação roda por vez. O **Histórico** mostra a situação da atual |
| Uma questão ficou de fora da importação | O relatório indica o arquivo e o motivo — sem alternativa correta, com mais de uma correta, com alternativa vazia, com menos de duas alternativas ou sem banca. Corrija o `.json` e envie de novo só os arquivos corrigidos |
| A importação falhou ao ser aplicada | Parte das questões pode ter sido gravada. Envie o mesmo zip de novo e simule: o relatório mostra o que ainda falta, e nada é duplicado |
| A importação gravou algo errado | Corrija as questões uma a uma, pela moderação. Para desfazer uma importação inteira, fale com quem mantém o servidor da plataforma |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Telas, botões, mensagens e fluxos | Código do frontend do `ifvest-monorepo` (commit `d36de12`): Área do Professor e Painel Administrativo | out/2026 |
| Regras de cadastro, edição e denúncia | [Descrição das Funcionalidades — Banco de questões](../../funcionalidades.md#banco-de-questoes), conferida no código do backend | out/2026 |
| Importação de questões | `docs/importar-questoes-pelo-painel.md`, no `ifvest-monorepo`, e [Descrição das Funcionalidades — Importar questões](../../funcionalidades.md#importar-questoes) | out/2026 |

!!! note "O que mudou em relação à versão anterior"
    A versão anterior desta página descrevia o banco de questões da plataforma anterior. No V3, não há questões dissertativas, a tela **Minhas questões** com as questões de cada professor, a **exclusão** de questões, a tela de **tópicos** nem a **verificação de similaridade** por inteligência artificial. O editor de equações em LaTeX também não existe: o conteúdo das questões usa Markdown.
