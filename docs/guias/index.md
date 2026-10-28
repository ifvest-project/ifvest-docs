# Guias de Uso do IFVest

Esta é a documentação de usuário do IFVest: como usar a plataforma, tarefa por tarefa. Escolha por onde começar.

| Se você... | Vá para | O que encontra |
|---|---|---|
| **Estuda** | [Guia do Aluno](aluno/index.md) | Praticar no IFQuiz e nos Simulados e acompanhar o seu desempenho |
| **Produz conteúdo** | [Guia do Professor](professor/index.md) | Cadastrar questões, criar simulados institucionais e importar provas |

**Todos** usam as mesmas páginas de conta:

- [Acesso e Conta](conta/acesso.md) — entrar com a conta Google e sair
- [Perfil e Seus Dados](conta/perfil.md) — apelido, indicadores e históricos de quizzes e simulados

O que cada pessoa pode fazer depende das **permissões** da conta, e não de um perfil escolhido no cadastro: um professor é, para a plataforma, alguém que tem as permissões de conteúdo. Ver [Descrição do Sistema — Perfis e permissões](../descricao-do-sistema.md#perfis-e-permissoes).

Os termos usados na plataforma estão no [Glossário](glossario.md).

---

## Qual versão da plataforma estes guias descrevem

!!! info "IFVest V3, em produção"
    Os guias descrevem a plataforma em produção, o **IFVest V3**, conferida no código em outubro de 2026 (commit `d36de12`).

    Eles foram escritos antes da entrega do V3, a partir dos relatórios do subprojeto de frontend, e revisados depois dela. Por isso, cada página registra também o que o design previa e não foi implementado. Os módulos **Revisão de Conteúdo** e **Flashcards** ainda não existem na plataforma: as páginas deles continuam nos guias, com um aviso no início, como registro do que foi planejado.

⬜ *Guias pendentes: Redação — escrever e enviar redações, propostas e correção — e Painel Administrativo — visão geral, usuários e permissões e módulos. O funcionamento dos dois está na [Descrição das Funcionalidades](../funcionalidades.md). A moderação e a importação de questões, que também ficam no painel, estão no [Banco de Questões](professor/banco-de-questoes.md).*

⬜ *Capturas de tela pendentes, a acrescentar com texto alternativo.*

---

## Como ler as tarefas

Cada tarefa dos guias segue a mesma estrutura, baseada na **ISO/IEC/IEEE 26514:2022** — *Design and development of information for users*:

| Campo | O que informa |
|---|---|
| **Status** | Se a tarefa está disponível na plataforma (ver legenda abaixo) |
| **Acesso** | Quem pode fazer a tarefa: qualquer pessoa, quem tem conta ou quem tem uma permissão específica |
| **Objetivo** | O que você realiza ao completar a tarefa |
| **Pré-requisitos** | O que precisa estar pronto antes |
| **Como fazer** | A sequência de passos, do início ao resultado, com os nomes que aparecem na tela |
| **Observações** | Limites, validações e situações comuns |

### Legenda de status

- ✅ **Disponível** — a tarefa funciona na plataforma em produção.
- 🔵 **Prevista** — a tarefa foi planejada, mas ainda não existe na plataforma.
- ⬜ **Pendência** — item aguardando confirmação ou material, como capturas de tela.

Os nomes de telas, botões e mensagens foram conferidos no código da plataforma. O design da interface pode mudar em versões futuras; quando isso acontecer, os guias serão atualizados.

---

## Acessibilidade da plataforma

Os ajustes de acessibilidade feitos pelo subprojeto responsável em 2025 — uso só com o teclado e com leitor de tela nos módulos de Simulados, Flashcards e IFQuiz, verificados num teste com um usuário cego, usando o NVDA — foram aplicados na **versão anterior** da plataforma. A interface do IFVest V3 foi reconstruída do zero, e não há avaliação de acessibilidade registrada sobre ela (ver [Requisitos Não-Funcionais — Usabilidade e acessibilidade](../requisitos/nao-funcionais.md#usabilidade-e-acessibilidade)).

*Fonte: relatório final do subprojeto de acessibilidade (2025).*

⬜ *A confirmar com o subprojeto de testes se a avaliação de 2026, descrita abaixo, cobre a interface do V3.*

### Normas de referência

A acessibilidade da plataforma é avaliada com base em dois referenciais adotados pelo projeto:

- **WCAG 2.2** (*Web Content Accessibility Guidelines*, W3C) — conjunto internacional de diretrizes organizado em quatro princípios: conteúdo perceptível, operável, compreensível e robusto.
- **ABNT NBR 17225:2025** — norma brasileira de acessibilidade em produtos e serviços digitais, alinhada às WCAG 2.2. Ela regulamenta o Art. 63 da Lei Brasileira de Inclusão da Pessoa com Deficiência (Lei nº 13.146/2015) e adota o **nível AA** de conformidade como padrão.

!!! note "Estas são as normas de referência, não uma declaração de conformidade"
    A avaliação de acessibilidade do IFVest está **em andamento**. As auditorias automatizadas, inspeções técnicas e validações manuais realizadas até o momento identificaram pontos a corrigir — entre eles estrutura semântica, contraste entre cores, navegação por teclado, hierarquia de cabeçalhos e uso de atributos de acessibilidade.

    Portanto, esta documentação registra **quais normas orientam o trabalho**, sem afirmar que a plataforma atende integralmente a um nível de conformidade.

*Fonte: estudo de benchmark e aplicação de ferramentas de avaliação de acessibilidade no IFVest, subprojeto de testes de software (2026).*

⬜ *A atualizar quando a avaliação de acessibilidade for concluída e houver resultado consolidado por nível de conformidade.*

### Convenções de acessibilidade destes guias

- Toda captura de tela terá **texto alternativo** descritivo.
- Os marcadores de status **nunca dependem apenas de símbolo ou cor**: vêm sempre acompanhados da palavra correspondente — Disponível, Prevista, Pendência.
- A hierarquia de títulos é consistente (página → tarefa) para permitir navegação por leitores de tela.

---

## Onde esta documentação se encaixa

Estes guias constituem o item **"Documentação de Usuário"** previsto no mapeamento da **ISO/IEC/IEEE 15289:2019** adotado pelo projeto, com estrutura e conteúdo conforme a **ISO/IEC/IEEE 26514:2022**. O registro de conformidade de cada guia — quais elementos da norma foram aplicados e quais foram adiados, com justificativa — está na página inicial do [Guia do Aluno](aluno/index.md#conformidade-com-as-normas) e do [Guia do Professor](professor/index.md#conformidade-com-as-normas).

Para o plano geral da documentação e as demais fases, ver [Planejamento da Documentação](../planejamento.md).
