# Acesso e Conta

Esta página reúne as tarefas de acesso à plataforma: entrar — o que, no primeiro acesso, também cria a sua conta — e sair. Ela vale para todos; o que cada pessoa pode fazer depois de entrar depende das [permissões](../../descricao-do-sistema.md#perfis-e-permissoes) da conta.

O IFVest **não tem senha própria**: a entrada é feita com a **conta Google**.

---

## Tarefa 1 — Entrar na plataforma

**Status:** ✅ Disponível  
**Acesso:** qualquer pessoa com uma conta Google

**Objetivo:** iniciar uma sessão para usar os módulos da plataforma. No primeiro acesso, a sua conta do IFVest é criada automaticamente.

**Pré-requisitos:** ter uma conta Google. Um e-mail institucional também serve, desde que seja uma conta Google.

**Como fazer:**

1. Na página inicial do IFVest (`ifvest.com.br`), clique em **Entrar**, no cabeçalho, ou em **Quero acessar a plataforma!**.
2. Na tela de entrada (`/login`), clique em **Entrar ou Cadastrar com Google**. O mesmo botão serve para o primeiro acesso e para os seguintes.
3. Na janela do Google, escolha a conta e confirme.
4. Você é levado à página **Início** (`/inicio`), com uma saudação pelo seu apelido e um cartão para cada módulo.

**Observações:**

- **No primeiro acesso**, a conta é criada a partir do e-mail da conta Google. Contas com e-mail `@ifsp.edu.br` recebem automaticamente as permissões de professor: cadastrar e editar questões, criar simulados institucionais e gerenciar os simulados de outras pessoas. As demais permissões são concedidas por um administrador.
- Nos acessos seguintes, a conta é reconhecida pelo mesmo e-mail. Entrar com outra conta Google cria outra conta no IFVest, sem o seu histórico.
- A janela do Google é aberta como janela separada do navegador (*pop-up*). Se ela não aparecer, permita as janelas do IFVest nas configurações do navegador.

---

## Tarefa 2 — Sair da plataforma

**Status:** ✅ Disponível  
**Acesso:** com conta

**Objetivo:** encerrar a sua sessão, especialmente em computadores compartilhados.

**Pré-requisitos:** ter entrado na plataforma.

**Como fazer:**

1. Clique em **Sair**, no canto direito do cabeçalho, ao lado de **Usuário**.
2. A sessão é encerrada, e você volta à página inicial pública.

**Observações:**

- Fechar a aba **não** encerra a sessão: ao abrir o IFVest de novo no mesmo navegador, você continua conectado. Em computador compartilhado, como no laboratório, use **Sair** ao terminar.
- Sair do IFVest não sai da sua conta Google no navegador. Em computador compartilhado, saia também da conta Google, para que a próxima pessoa não a encontre aberta.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| As telas aparecem com zeros ou listas vazias | A sua sessão pode ter terminado. As telas internas abrem mesmo sem login, mas os dados só carregam para quem entrou: entre de novo ([Tarefa 1](#tarefa-1-entrar-na-plataforma)) |
| A janela do Google não abriu | O navegador pode estar bloqueando janelas *pop-up*. Permita as janelas do IFVest e clique de novo no botão |
| Esqueci a minha senha | O IFVest não tem senha própria. Recupere a senha da sua conta Google pelo próprio Google |
| Entrei, mas não vejo as abas **Professor** ou **Admin** | Elas aparecem só para quem tem as permissões correspondentes, logo depois que a plataforma as carrega. Se você deveria tê-las, peça a um administrador |
| Ação recusada por falta de permissão | A mensagem *"Você não tem a permissão '…' para concluir esta ação"* indica a permissão que falta à sua conta. Peça-a a um administrador |

---

## O que mudou em relação ao planejado

O design do subprojeto de frontend previa, além da entrada pelo Google, o **cadastro por formulário**, com nome de usuário e senha, e a **recuperação de senha** em três etapas — informar o e-mail, validar um código e definir a nova senha. O IFVest V3 adotou **só a entrada pela conta Google**, e por isso essas tarefas não existem: não há senha do IFVest a cadastrar nem a recuperar.

Os requisitos dessas funcionalidades continuam registrados como não atendidos em [Requisitos Funcionais — Conta e acesso](../../requisitos/funcionais.md#conta-e-acesso).

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Telas, botões e fluxos | Código do frontend do `ifvest-monorepo` (commit `d36de12`): página inicial, tela de entrada, cabeçalho e sessão | out/2026 |
| Criação da conta e permissões iniciais | [Descrição das Funcionalidades — Conta e acesso](../../funcionalidades.md#conta-e-acesso), conferida no código do backend | out/2026 |
| Design anterior: cadastro por formulário e recuperação de senha | Relatório 1 — Maria Luiza, subprojeto *Refatoração para React e Redesign do IFVest*, itens 2 e 3 | abr/2026 |
