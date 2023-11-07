import requests


def buscar_usuario(usuario):
    url = f'https://api.github.com/users/{usuario}'
    resposta = requests.get(url)
    return resposta.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_usuario('Marcondysbezerra'))
