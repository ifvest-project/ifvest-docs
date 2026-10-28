# Requisitos Não-Funcionais

Esta página registra como o IFVest deve se comportar — desempenho, segurança, usabilidade e qualidade do código —, independentemente da funcionalidade em uso. Como os [Requisitos Funcionais](funcionais.md), está organizada em dois níveis:

- **[Requisitos da plataforma](#requisitos-da-plataforma)** — valem para o IFVest como um todo. Partem da versão anterior desta especificação, atualizada para o IFVest V3, e dos critérios de qualidade que a equipe de desenvolvimento adotou no repositório da plataforma.
- **[Requisitos por módulo](#requisitos-por-modulo)** — citados pelas equipes no Levantamento de Funcionalidades e Regras de Negócio.

---

## Como ler esta página

- **ID** — os requisitos da plataforma são identificados por `RNFG`, de *requisito não-funcional geral*. De RNFG01 a RNFG12, o número é o mesmo da especificação anterior: o RNFG01 corresponde ao antigo RNF01, e assim por diante. Os requisitos por módulo mantêm o identificador usado pela equipe no levantamento.
- **Situação no V3**:

| Situação | Significado |
|---|---|
| ✅ Atendido | A plataforma cumpre o requisito, conforme medição ou verificação registrada |
| 🟡 Em parte | A plataforma cumpre parte do requisito; a observação explica |
| ⬜ Não atendido | A plataforma não cumpre o requisito |
| ❔ A verificar | Não há medição ou verificação registrada que permita dizer se o requisito é cumprido |

---

## Requisitos da plataforma

Os requisitos de RNFG01 a RNFG12 vêm da especificação anterior, atualizados para o V3; o RNFG13 e o RNFG14 vêm dos critérios de qualidade da equipe de desenvolvimento.

### Desempenho e capacidade

Relacionados ao subprojeto de [Testes Não-Funcionais](../subprojetos/qualidade-e-testes.md#testes-nao-funcionais).

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| RNFG01 | **Tempo de resposta.** As páginas principais devem carregar em menos de 2 segundos, em conexões de banda larga estáveis. | ❔ A verificar | Sem medição registrada. A plataforma roda num único servidor próprio: ver [Arquitetura — Topologia de produção](../arquitetura.md#topologia-de-producao). |
| RNFG02 | **Carga e escalabilidade.** A plataforma deve suportar até 500 usuários simultâneos sem degradação perceptível de desempenho, medida com o JMeter. | ❔ A verificar | Sem teste de carga registrado. |
| RNFG03 | **Eficiência do banco de dados.** As consultas complexas ao banco de questões devem retornar resultados em menos de 500 ms. | ❔ A verificar | Sem medição registrada. |

### Segurança e privacidade

Relacionados ao subprojeto de [Adequação do Cadastro à LGPD](../subprojetos/infra-e-seguranca.md#adequacao-do-cadastro-da-ifvest-a-lgpd).

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| RNFG04 | **Proteção de dados (LGPD).** O sistema deve isolar os dados dos usuários, garantindo que cada um acesse apenas as próprias informações. | ❔ A verificar | No V3, os dados ficam no PostgreSQL, e o acesso a eles é controlado pela API. As *Security Rules* do Firebase, previstas na especificação anterior, não se aplicam, porque o Firebase é usado só na autenticação. A plataforma ainda não publica uma política de privacidade. |
| RNFG05 | **Senhas.** Nenhuma senha deve ser armazenada em texto plano. | ✅ Atendido | A plataforma não recebe nem armazena senhas: a entrada é feita pela conta Google, autenticada pelo Firebase Authentication. |
| RNFG06 | **Controle de acesso.** O sistema deve aplicar regras formais de controle de acesso, verificadas no servidor, para diferenciar o que cada usuário pode fazer. | ✅ Atendido | Por permissões individuais, sem perfis fixos ([RFG04](funcionais.md#rfg04)): cada operação protegida da API exige a permissão correspondente, definida num catálogo único. A especificação anterior previa perfis fixos de aluno, professor e administrador. |

### Usabilidade e acessibilidade

Relacionados aos subprojetos de [Acessibilidade](../subprojetos/qualidade-e-testes.md#implementacao-de-melhorias-de-acessibilidade) e de [Interface](../subprojetos/frontend.md).

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| RNFG07 | **Acessibilidade.** A interface deve atingir ao menos 90 de 100 pontos em ferramentas de auditoria automatizada de acessibilidade, como o Axe Core e o Lighthouse. | ❔ A verificar | Sem auditoria registrada. O repositório da plataforma não inclui essas ferramentas. |
| RNFG08 | **Estética e design.** O sistema deve seguir o guia de estilos e componentes definido no Figma, com consistência visual entre os módulos. | ❔ A verificar | O repositório da plataforma não faz referência ao guia. |
| RNFG09 | **Apreensibilidade.** Um novo usuário deve conseguir fazer o primeiro simulado ou quiz sem consultar manuais. | ❔ A verificar | Sem teste de usabilidade registrado. |

### Manutenibilidade e confiabilidade

Relacionados ao subprojeto de [Testes Funcionais e Mutantes](../subprojetos/qualidade-e-testes.md#testes-funcionais-e-mutantes). A integração contínua verifica estes limites a cada alteração no repositório da plataforma (ver [Arquitetura — Qualidade e testes](../arquitetura.md#qualidade-e-testes)), e a situação abaixo é a das últimas medições registradas pela equipe, de setembro de 2026.

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| RNFG10 | **Cobertura de testes.** Os testes devem cobrir ao menos 90% do código: no backend, em linhas e ramos; no frontend, em linhas, ramos, funções e instruções. | ✅ Atendido | 98% no backend; no frontend, de 90,9% a 97,3%, conforme a medida. A especificação anterior pedia mais de 80%, só no código crítico do backend. |
| RNFG11 | **Testes de mutação.** O código deve passar por testes de mutação, que verificam se os testes existentes detectam falhas reais. | 🟡 Em parte | Rodam toda segunda-feira e sob demanda. No frontend, o Stryker detectou 89,7% dos mutantes na primeira medição, acima do mínimo de 60%. No backend, o mutmut foi ajustado em 15/10/2026 para rodar na integração contínua e ainda não tem medição registrada. |
| RNFG12 | **Padronização do código.** O código deve seguir as regras de estilo e de análise estática da equipe, com complexidade de até 9 por função. | ✅ Atendido | No frontend, ESLint sem avisos e TypeScript sem erros de tipo, com complexidade cognitiva de até 9; no backend, Ruff sem erros de lint e de formatação, com complexidade ciclomática de até 9. A especificação anterior previa só o ESLint, no frontend. |
| RNFG13 | **Migrations.** Toda mudança no modelo de dados deve vir com uma migration aplicável e reversível, correspondente aos modelos. | ✅ Atendido | Verificado sobre PostgreSQL. |
| RNFG14 | **Testes de ponta a ponta.** As jornadas principais da plataforma devem ter testes de ponta a ponta, executados sobre PostgreSQL, todos passando. | ✅ Atendido | Com o Playwright, num navegador real. |

⬜ *Verificação não obrigatória: a integração contínua só impede a entrada de código fora destes limites se a proteção da branch principal estiver configurada no GitHub, o que ainda não foi confirmado. Ver [Arquitetura — Pontos de atenção](../arquitetura.md#pontos-de-atencao).*

---

## Requisitos por módulo

Os requisitos não-funcionais do **Levantamento de Funcionalidades e Regras de Negócio** aparecem citados pelo número nas entradas do IFQuiz. A tabela reúne o que cada citação afirma e onde aparece. O levantamento ainda não trata dos requisitos não-funcionais dos demais módulos.

### IFQuiz

| ID | Requisito | Situação no V3 | Observação |
|---|---|---|---|
| RNF1 | Tempo de resposta de até 2 segundos: na sincronização das respostas entre os dois jogadores do modo competição e na resposta do ranking. | ❔ A verificar | Citado no Modo Competição (#004) e no Ranking (#007). Sem medição registrada; o modo competição ainda não existe ([RF6 do IFQuiz](funcionais.md#ifquiz)). |
| RNF2 | Suporte a muitos registros sem perda de desempenho. | ❔ A verificar | Citado no Ranking (#007). Sem medição registrada. |
| RNF3 | Disponibilidade de 99,9%, contínua, para que o usuário não perca a Pergunta do Dia e o cálculo diário da sequência não seja afetado. | ❔ A verificar | Citado na Pergunta do Dia (#003) e na Sequência diária (#005). Sem medição registrada; a plataforma roda num único servidor. |
| RNF5 | Citado a respeito da exibição correta do avatar em navegadores diferentes; o enunciado não aparece no levantamento. | ❔ A verificar | Citado em Avatares e loja (#008). |
| RNF6 | Pontuações e resultados salvos imediatamente após cada resposta, para que não haja perda de dados em caso de falha. | 🟡 Em parte | Citado na Validação de respostas (#002) e no Histórico (#009). Cada resposta é gravada no momento em que é dada, mas os pontos do quiz são somados ao saldo só ao fim da partida. |

⬜ *Obter com a equipe do IFQuiz a lista completa: o levantamento cita os requisitos pelo número, mas não traz a lista, e o RNF4 não é citado.*

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Requisitos da plataforma, de RNFG01 a RNFG12 | Versão anterior desta página, preservada na etiqueta `legado-v2` | ago/2026 |
| Limites de qualidade do código e medições | `docs/quality-gates-2026-09-27.md`, `docs/auditoria-testes-2026-09-25.md` e configuração da integração contínua do `ifvest-monorepo` | set/2026, revisto em out/2026 |
| Requisitos por módulo | Levantamento de Funcionalidades e Regras de Negócio, entradas do IFQuiz | 20/10/2026 |
| Situação na plataforma | Código e configuração de produção do `ifvest-monorepo` | out/2026 |
