import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '65560870bf7f1bb861b0c3a2f2279d52'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : '65560870bf7f1bb861b0c3a2f2279d52'}

body = {
    "name": "Лео",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_name = {
    "pokemon_id": "14462",
    "name": "Зубр",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokeball = {
    "pokemon_id": "14462"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body_name)
print(response_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_add_pokeball)
print(response_add_pokeball.text)

