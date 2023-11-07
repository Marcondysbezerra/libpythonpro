from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import sessao


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Marcondys')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Marcondys'), Usuario(nome='Bruna')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

