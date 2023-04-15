from flask import Flask, render_template, request
import pokeapi as pk
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def pokedex(name = None):
    dados_pokemon = pk.pega_pokemon(name)
    return render_template('index.html', dados_pokemon = dados_pokemon)
    
if __name__ == '__main__':
    app.run(debug=True)