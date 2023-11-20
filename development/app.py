from flask import Flask, render_template
import markdown2
from os import path

app = Flask(__name__)

@app.route('/')
def index():

    # Caminho para o arquivo Markdown
    md_file_path = path.join(path.dirname(__file__), 'markdown\pagina.md')

    # Carregue o conteúdo do arquivo Markdown
    with open(md_file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    # Converte o conteúdo Markdown para HTML
    html_content = markdown2.markdown(markdown_content)

    # Renderiza o template HTML com o conteúdo Markdown convertido
    return render_template('index.html', target=html_content)

if __name__ == '__main__':
    app.run(debug=True)





