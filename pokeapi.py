import requests

def pega_pokemon(name):
    if name == None:
        return ' '
    url = f'https://pokeapi.co/api/v2/pokemon/{name}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        dados_pokemon = {
            'nome' : data['name'],
            'id' : data['id'],
            'tipo' : [],
            'sprite' : data['sprites']['front_default'],
            'spriteanimated' : data['sprites']['versions']['generation-v']['black-white']['animated']['front_default']
        }
        for i in data['types']:
            dados_pokemon['tipo'].append(i['type']['name'])
    return dados_pokemon
