from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import sessao


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Marcondys', email='marcondysb@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Marcondys', email='marcondysb@gmail.com'),
                Usuario(nome='Bruna', email='marcondysb@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

