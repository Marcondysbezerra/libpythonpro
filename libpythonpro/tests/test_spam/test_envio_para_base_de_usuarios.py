from unittest.mock import Mock

import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Marcondys', email='marcondysb@gmail.com'),
            Usuario(nome='Bruna', email='marcondysb@gmail.com')
        ],

        [
            Usuario(nome='Bruna', email='marcondysb@gmail.com')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'brubav@gmail.com',
        'Curso Python Pro',
        'Confira os módulos do curso.'
    )
    assert len(usuarios) == enviador.enviar.call_count


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_emails_enviados = 0
        self.paramentros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_emails_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Bruna', email='marcondysb@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'brunav@gmail.com',
        'Curso Python Pro',
        'Confira os módulos do curso.'
    )
    enviador.enviar.assert_called_once_with(
        'brunav@gmail.com',
        'marcondysb@gmail.com',
        'Curso Python Pro',
        'Confira os módulos do curso.'

    )