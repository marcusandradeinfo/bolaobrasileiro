import markdown
from bs4 import BeautifulSoup
import mistune
import os


def ConvertMarkdownToHTML():
    # Ler o arquivo Markdown
    caminho = os.path.join("static", "markdown", "regulamento.md")
    with open(caminho, "r", encoding="utf-8") as md_file:
        md_text = md_file.read()

    # Converter para HTML5
    html_content = markdown.markdown(md_text, extensions=['extra', 'toc', 'codehilite'])
    return html_content


def ConvertMarkdownToText():
    """Converte Markdown para texto puro, removendo formatação."""

    caminho_arquivo = os.path.join("static", "markdown", "regulamento.md")

    # Abre o arquivo Markdown e lê o conteúdo
    with open(caminho_arquivo, "r", encoding="utf-8") as md_file:
        markdown_texto = md_file.read()

    # Converte Markdown para HTML
    markdown_parser = mistune.create_markdown(renderer="html")
    html = markdown_parser(markdown_texto)

    # Remove tags HTML para obter texto puro
    from bs4 import BeautifulSoup
    texto_bruto = BeautifulSoup(html, "html.parser").get_text()

    return texto_bruto
