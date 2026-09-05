# Importar

from flask import Flask, render_template, request


app = Flask(__name__)


# Conteúdo da página
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades Dinâmicas
@app.route('/', methods=['POST'])
def process_form():

    button_python = request.form.get('button_python')
    button_java = request.form.get('button_java')
    button_postgresql = request.form.get('button_postgresql')
    button_html = request.form.get('button_html')
    button_css = request.form.get('button_css')

    # Formulário de contato
    email = request.form.get('email')
    text = request.form.get('text')

    # Mostra o feedback no terminal
    if email and text:
        print("Novo feedback:")
        print("E-mail:", email)
        print("Mensagem:", text)

    return render_template(
        'index.html',
        button_python=button_python,
        button_java=button_java,
        button_postgresql=button_postgresql,
        button_html=button_html,
        button_css=button_css
    )


if __name__ == "__main__":
    app.run(debug=True)