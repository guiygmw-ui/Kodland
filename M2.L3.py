from flask import Flask
import random
import string

app = Flask(__name__)

facts_list = [
    "A maioria das pessoas que sofre de dependência tecnológica sente um forte estresse quando fica fora da área de cobertura de rede ou não pode usar seus dispositivos.",
    "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.",
    "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna.",
    "Segundo um estudo de 2019, mais de 60% das pessoas respondem a mensagens de trabalho em seus smartphones dentro de 15 minutos após sair do trabalho.",
    "Uma forma de combater a dependência tecnológica é buscar atividades que tragam prazer e melhorem o humor.",
    "As redes sociais são projetadas para manter os usuários o máximo de tempo possível consumindo conteúdo.",
    "As redes sociais têm pontos positivos e negativos, e devemos utilizá-las com equilíbrio."
]

@app.route("/")
def home():
    return """
    <h1>Bem-vindo ao site sobre Dependências Tecnológicas!</h1>
    <p>Escolha uma das opções abaixo:</p>

    <a href="/random_fact">📖 Ver um fato aleatório</a><br><br>

    <a href="/secret">🔐 Página Secreta</a>
    """

@app.route("/random_fact")
def random_fact():
    return f"""
    <h1>📖 Fato Aleatório</h1>

    <p>{random.choice(facts_list)}</p>

    <br>

    <a href="/">⬅ Voltar para a página inicial</a>
    """

@app.route("/secret")
def secret():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(12))

    return f"""
    <h1>🔐 Página Secreta</h1>

    <p>Sua senha aleatória é:</p>

    <h2>{senha}</h2>

    <a href="/">⬅ Voltar para a página inicial</a>
    """

app.run(debug=True)
