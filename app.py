from flask import Flask, render_template, request
import pokeapi as pk
app = Flask(__name__)

dados_pokemon = {
        'nome' : 'charizard',
        'id' : 6,
        'tipo' : ['fire', 'flight'],
        'sprite' : 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/6.png',
        'spriteanimated' : 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/6.gif'
    }

@app.route('/')
def index():
    return render_template('home.html', dados_pokemon = dados_pokemon)

@app.route('/process_form', methods = ['POST'])
def process_form():
    name = request.form['pokemon']
    dados_pokemon = pk.pega_pokemon(name)
    imagem1 = dados_pokemon['sprite']
    imagem2 = dados_pokemon['spriteanimated']
    return render_template('home.html', dados_pokemon = dados_pokemon, imagem1 = imagem1, imagem2 = imagem2)

if __name__ == '__main__':
    app.run(debug=True)