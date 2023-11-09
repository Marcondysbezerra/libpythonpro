from unittest.mock import Mock

import pytest

from libpythonpro import githubapi


def test_buscar_avatar(avatar_url):
    url = githubapi.buscar_usuario('Marcondysbezerra')
    assert avatar_url == url


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/48830573?v=4'
    resp_mock.json.return_value = {
        "login": "Marcondysbezerra",
        "id": 48830573,
        "avatar_url": url,
    }
    get_mock = mocker.patch('libpythonpro.githubapi.requests.get')
    get_mock.return_value = resp_mock
    return url



def test_buscar_avatar_integracao():
    url = githubapi.buscar_usuario('Marcondysbezerra')
    assert 'https://avatars.githubusercontent.com/u/48830573?v=4' == url