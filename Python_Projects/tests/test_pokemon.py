import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '2574'

def test_status_code_200():
    response = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response.status_code ==200

def test_part_of_responce():
    response_get = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_get.json()['data'] [0]['trainer_id']=='2574'


@pytest.mark.parametrize('key, value', [('name', 'OMOMO'),('trainer_id', TRAINER_ID)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url=f'{URL}/pokemons', params={'trainer_id': TRAINER_ID})
    assert response_parametrize.json()['data'][0][key]== value