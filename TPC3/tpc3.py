import re
import sys

def convert_headers(markdown):
    # Converte cabeçalhos (#, ##, ###) para <h1>, <h2>, <h3>
    markdown = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    return markdown

def convert_bold(markdown):
    # Converte **texto** para <b>texto</b>
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    return markdown

def convert_italic(markdown):
    # Converte *texto* para <i>texto</i>
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)
    return markdown

def convert_links(markdown):
    # Converte [texto](URL) para <a href="URL">texto</a>
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)
    return markdown

def convert_images(markdown):
    # Converte ![texto](URL) para <img src="URL" alt="texto"/>
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', markdown)
    return markdown

def convert_lists(markdown):
    # Converte listas numeradas para <ol> e <li>
    lines = markdown.split('\n')
    in_list = False
    for i, line in enumerate(lines):
        if re.match(r'^\d+\.\s+(.*)$', line):
            if not in_list:
                lines[i] = '<ol>\n<li>' + re.sub(r'^\d+\.\s+(.*)$', r'\1', line) + '</li>'
                in_list = True
            else:
                lines[i] = '<li>' + re.sub(r'^\d+\.\s+(.*)$', r'\1', line) + '</li>'
        else:
            if in_list:
                lines[i-1] += '\n</ol>'
                in_list = False
    if in_list:
        lines[-1] += '\n</ol>'
    return '\n'.join(lines)

def markdown_to_html(markdown):
    markdown = convert_headers(markdown)
    markdown = convert_bold(markdown)
    markdown = convert_italic(markdown)
    markdown = convert_links(markdown)
    markdown = convert_images(markdown)
    markdown = convert_lists(markdown)
    return markdown

def main():
    text = []
    try:
        while True:
            line = input()
            text.append(line)
    except EOFError:
        pass  # Finaliza a leitura ao detectar Ctrl+D (EOF)
    # Junta as linhas numa única string
    # Pressionar as teclas ctrl+D para terminar a string
    markdown_text = '\n'.join(text)
    html_output = markdown_to_html(markdown_text)
    print(html_output)

if __name__ == '__main__':
    main()
