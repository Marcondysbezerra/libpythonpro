import requests


def buscar_usuario(usuario):
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']

buscar_usuario('Marcondysbezerra')