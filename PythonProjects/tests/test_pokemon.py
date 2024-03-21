import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '65560870bf7f1bb861b0c3a2f2279d52'
HEADERS = {'Content-Type' : 'application/json', 'trainer_token' : '65560870bf7f1bb861b0c3a2f2279d52'}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : 122})
    assert response.status_code == 200

def test_part_of_response():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : 122})
    assert response.json()['data'][0]['trainer_name'] == 'Yana'