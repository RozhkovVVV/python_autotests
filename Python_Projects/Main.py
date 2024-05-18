import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_create = {
    "name": "ShanSung",
    "photo": "https://dolnikov.ru/pokemons/albums/711.png"
}


responce_create = requests.post(url=f'{URL}/pokemons', headers=HEADER, json = body_create)
print(responce_create.text)

id_pokemon = responce_create.json()['id']
print(id_pokemon)

body_change = {
    "pokemon_id": id_pokemon,
    "name": "OMOMO",
    "photo": "https://dolnikov.ru/pokemons/albums/712.png"
}

body_pokeball = {
    "pokemon_id": id_pokemon,
}


responce_change = requests.put(url=f'{URL}/pokemons', headers=HEADER, json = body_change)
print(responce_change.text)

responce_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json = body_pokeball)
print(responce_pokeball.text)

