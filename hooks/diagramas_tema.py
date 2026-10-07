"""Gera cada diagrama C4 em duas versões, uma para o tema claro e outra para o escuro.

O PlantUML devolve uma imagem com as cores fixas: fundo branco, linhas e textos escuros.
No tema escuro do site, ela aparecia como um bloco branco. Este hook roda no build, antes
de o Markdown ser convertido, e troca cada bloco ```plantuml de diagrama C4 por:

    <div class="diagrama-c4">
    ```plantuml classes="uml c4_claro"   -> versão clara, como está na página
    ```plantuml classes="uml c4_escuro"  -> versão escura: fundo transparente e linhas,
    </div>                                  textos e legenda claros

O diagrama continua escrito uma vez só, na página. O CSS em docs/stylesheets/extra.css
põe as duas imagens no mesmo lugar, uma sobre a outra, e deixa visível só a do tema ativo.
Como as duas ocupam sempre o mesmo espaço, trocar o tema não muda a altura da página, e a
troca é imediata, porque as duas imagens já estão carregadas.

O <div> pode ser HTML puro porque o plantuml_markdown (prioridade 30) troca os blocos
pelas imagens antes de o Markdown separar os blocos HTML (prioridade 20).

As variáveis de cor só são conhecidas pelo C4-PlantUML; por isso, blocos que não incluem o
C4 ficam como estão. Também ficam como estão os blocos que já têm opções na abertura
(classes, alt etc.), para não sobrescrever o que foi escolhido à mão.
"""

import re

# O endereço de cada imagem no servidor PlantUML é o próprio texto do diagrama compactado,
# e o servidor público (plantuml.com) permite que a imagem de um endereço fique guardada
# em cache por até 5 dias. Este número entra como comentário nas duas versões: se o
# servidor devolver um diagrama quebrado (caixas estreitas, palavras umas sobre as outras),
# aumentá-lo muda o endereço de todos os diagramas e força um desenho novo. O desenho em si
# não muda.
REVISAO = 1

# Usa a forma !$VAR = valor, que precisa vir ANTES do !include: o C4-PlantUML define
# as suas cores com ?=, que só atribui quando a variável ainda não existe.
ESTILO_ESCURO = """\
!$ARROW_COLOR = "#B5B3C1"
!$BOUNDARY_COLOR = "#C9C6D3"
!$LEGEND_TITLE_COLOR = "#E6E3EE"
!$PERSON_BORDER_COLOR = "#3C7FC0"
skinparam backgroundColor transparent
skinparam titleFontColor #E6E3EE
"""

BLOCO_PLANTUML = re.compile(
    r"^(?P<cerca>```|~~~)[ \t]*plantuml[ \t]*\n(?P<fonte>.*?\n)(?P=cerca)[ \t]*$",
    re.MULTILINE | re.DOTALL,
)
TITULO = re.compile(r"^\s*title\s+(?P<titulo>.+?)\s*$", re.MULTILINE)


def versao(fonte: str, tema: str, estilo: str = "") -> str:
    """Insere, logo depois da linha @startuml, a marca da versão e o estilo do tema."""
    marca = f"' Versão do tema {tema}, gerada por hooks/diagramas_tema.py (revisão {REVISAO})\n"
    linhas = fonte.splitlines(keepends=True)
    for posicao, linha in enumerate(linhas):
        if linha.lstrip().startswith("@startuml"):
            return "".join(linhas[: posicao + 1]) + marca + estilo + "".join(linhas[posicao + 1 :])
    return marca + estilo + fonte


def texto_alternativo(fonte: str) -> str:
    """Usa o título do diagrama como texto alternativo da imagem."""
    titulo = TITULO.search(fonte)
    texto = titulo.group("titulo") if titulo else "Diagrama C4"
    return texto.replace('"', "").replace("'", "")


def duplicar(bloco: re.Match) -> str:
    cerca, fonte = bloco.group("cerca"), bloco.group("fonte")
    if "C4_" not in fonte:
        return bloco.group(0)
    alt = texto_alternativo(fonte)
    return (
        '\n<div class="diagrama-c4">\n'
        f'{cerca}plantuml classes="uml c4_claro" alt="{alt}"\n{versao(fonte, "claro")}{cerca}\n'
        f'{cerca}plantuml classes="uml c4_escuro" alt="{alt}"\n'
        f'{versao(fonte, "escuro", ESTILO_ESCURO)}{cerca}\n'
        "</div>\n"
    )


def on_page_markdown(markdown: str, **kwargs) -> str:
    return BLOCO_PLANTUML.sub(duplicar, markdown)
