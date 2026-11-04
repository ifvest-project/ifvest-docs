# Importação de Questões

As provas de vestibular entram no banco de questões em lote, a partir dos arquivos gerados pela extração das provas. Na aba **Importar Questões** do Painel Administrativo, o administrador envia esses arquivos num `.zip`, confere numa **simulação** o que vai acontecer e só então **aplica** a importação.

A importação pelo painel faz o mesmo que a carga feita por linha de comando no servidor, descrita em [Arquitetura — Carga do banco de questões](../../arquitetura.md#carga-do-banco-de-questoes).

---

## Tarefa 1 — Importar questões em lote

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
    | **Substituir também as questões corrigidas à mão pela moderação** | Desmarcada | Aplica o zip também às questões editadas à mão, na moderação ou no banco de questões. Só pode ser marcada junto com a anterior |

4. Clique em **Enviar e simular**. A plataforma lê o zip e mostra o que **aconteceria**, sem gravar nada: quantas questões **Serão inseridas** e quantas **Serão corrigidas**, o que mudaria em cada questão corrigida, as **Questões com problema, que ficam de fora**, as **Imagens que faltam no zip** e os **Arquivos que não puderam ser lidos**. Em arquivos grandes, a simulação leva alguns minutos, e a tela se atualiza sozinha.
5. Quando aparecer *"Simulação concluída. Nada foi gravado ainda."* e o relatório estiver como esperado, clique em **Aplicar importação**. A plataforma grava exatamente o que a simulação mostrou.
6. Aguarde *"Importação aplicada."* Enquanto ela roda, você pode sair da página: a importação continua no servidor, e o andamento fica no histórico ([Tarefa 2](#tarefa-2-acompanhar-o-historico-de-importacoes)).

!!! warning "Não desfaça as correções feitas à mão"
    Deixe desmarcada a opção **Substituir também as questões corrigidas à mão pela moderação**, a menos que o zip traga uma versão melhor dessas questões. Marcada, ela sobrescreve as correções feitas pelos professores e pelos administradores. A simulação lista as questões protegidas em **Questões corrigidas pela moderação, que ficam como estão**.

**Observações:**

- **Limites:** 300 MB por arquivo, 1 GB descompactado e 50 mil arquivos. Acima disso, divida as provas em mais de um zip.
- Só entram questões completas: ao menos duas alternativas, todas com texto ou imagem, e exatamente uma correta. As demais aparecem no relatório, com o motivo, até que o arquivo seja corrigido.
- As questões discursivas do zip não entram: o banco tem só questões de múltipla escolha.
- Uma questão sem a figura no zip entra, mas a figura não aparece. O relatório lista as imagens que faltam.
- Os textos compartilhados por várias questões viram o texto de apoio de cada uma.
- As questões importadas chegam sem resolução. Ela pode ser escrita depois, pela edição da questão.
- Para corrigir questões que já estão no banco, o zip pode ter só os arquivos corrigidos, na pasta da respectiva prova.
- Só uma importação roda por vez. O zip fica guardado por 24 horas; depois disso, ou se o servidor reiniciar, é preciso enviá-lo de novo para aplicar.
- A importação nunca remove questões.

---

## Tarefa 2 — Acompanhar o histórico de importações

**Status:** ✅ Disponível  
**Acesso:** `admin_permission`

**Objetivo:** conferir a situação das importações e reabrir o relatório de cada uma.

**Pré-requisitos:** ter a permissão de administrador.

**Como fazer:**

1. Na aba **Importar Questões**, desça até o **Histórico**. A tabela lista as importações mais recentes:

    | Coluna | O que mostra |
    |---|---|
    | **#** | O número da importação |
    | **Data** | Quando o zip foi enviado |
    | **Arquivo** | O nome do zip |
    | **Tipo** | **Simulação** ou, para uma importação aplicada, **Aplicação da #** e o número da simulação |
    | **Situação** | **Na fila**, **Rodando**, **Concluída** ou **Falhou** |
    | **Enviado por** | Quem enviou |
    | **Relatório** | O botão **Ver relatório #**, que reabre o relatório |

2. Clique em **Ver relatório #…** para rever os números e as listas daquela importação. Numa simulação concluída que ainda não foi aplicada, e cujo zip continua guardado, o relatório traz de novo o botão **Aplicar importação**.

**Observações:**

- Cada importação aplicada fica também no registro de auditoria (ver [Indicadores e Auditoria](indicadores-e-auditoria.md#tarefa-2-acompanhar-as-modificacoes-recentes)).

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| *"Aguarde a importação em andamento terminar para enviar outro arquivo."* | Só uma importação roda por vez. O **Histórico** mostra a situação da atual |
| *"A simulação não encontrou nenhuma questão para inserir ou corrigir."* | As questões do zip já estão no banco, iguais, ou ficaram todas de fora. Confira as listas do relatório e a opção **Corrigir as questões que já estão no site** |
| Uma questão ficou de fora da importação | O relatório indica o arquivo e o motivo — sem alternativa correta, com mais de uma correta, com alternativa vazia, com menos de duas alternativas ou sem banca. Corrija o `.json` e envie de novo só os arquivos corrigidos |
| *"A importação falhou."* | Parte das questões pode ter sido gravada. Envie o mesmo zip de novo e simule: o relatório mostra o que ainda falta, e nada é duplicado |
| A importação gravou algo errado | Corrija as questões uma a uma, pela edição. Para desfazer uma importação inteira, fale com quem mantém o servidor da plataforma |

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tela, opções, mensagens e histórico | Código do frontend do `ifvest-monorepo` (commit `73c9098`): Painel Administrativo, aba Importar Questões | out/2026 |
| Processo, limites e regras da importação | `docs/importar-questoes-pelo-painel.md`, no `ifvest-monorepo`, e [Descrição das Funcionalidades — Importar questões](../../funcionalidades.md#importar-questoes) | out/2026 |
| Proteção das questões editadas à mão | `ifvest-backend/src/services/unicamp_question_update.py`, no `ifvest-monorepo` | out/2026 |
