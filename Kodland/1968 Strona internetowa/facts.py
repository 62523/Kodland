from flask import Flask
import random

app = Flask(__name__)


facts_list = ["Elon Musk twierdzi, że sieci społecznościowe zostały zaprojektowane tak, aby trzymać nas na platformie, abyśmy spędzali jak najwięcej czasu na przeglądaniu treści.",
             "Według badania przeprowadzonego w 2018 r. ponad 50% osób w wieku od 18 do 34 lat uważa, że jest zależnych od swoich smartfonów.",
             "Sieci społecznościowe mają swoje zalety i wady, a korzystając z tych platform, powinniśmy być ich świadomi.",
             "Badanie uzależnień technologicznych jest jednym z najważniejszych obszarów współczesnych badań naukowych."]


@app.route("/")
def index():
    return f'''<h1>Cześć! Na tej stronie możesz dowiedzieć się kilku ciekawostek na temat zależności technologicznych!</h1><br>
    <a href="/random_fact">Treść mojego linku do podstrony o faktach</a>
    '''

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)