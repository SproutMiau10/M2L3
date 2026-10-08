import random
from flask import Flask

app = Flask(__name__)

facts_list = [
    "Impacto emocional: A dependência tecnológica pode causar sintomas de abstinência quando a tecnologia não está disponível, como ansiedade e desconforto. Procure equilibrar o uso da tecnologia com atividades offline para lidar melhor com esse tipo de situação.",
    "Uso compulsivo de dispositivos e redes sociais está associado a ansiedade, depressão, isolamento social e baixa autoestima.",
    "Notificações constantes e multitarefa midiática fragmentam o foco e sobrecarregam o córtex pré-frontal.",
    "A dependência tecnológica pode levar a problemas de sono, como insônia e dificuldade em adormecer, devido à exposição prolongada a telas e à luz azul emitida por dispositivos eletrônicos.",
    "A dependência tecnológica pode afetar negativamente a memória e a capacidade de concentração."
]

secret_list = ["Cara!", "Coroa!", "Tijolo :3"]

@app.route("/")
def index():
    return f'<h1>Olá! Nessa página você encontrará algumas informações sobre dependências tecnológicas!</h1> <a href="/random_fact">Veja um fato aleatório!</a> <a href="/secrets">Segredos!</a>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/secrets")
def secret():
    return f'<p>{random.choice(secret_list)}</p>'

app.run(debug=True)
