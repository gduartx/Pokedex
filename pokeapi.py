import requests

def pega_pokemon(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dados_pokemon = {
            'nome' : data['name'],
            'id' : data['id'],
            'sprite' : data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
        }
    return dados_pokemon
