import pytest

from libpythonpro.spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    conexao_obj.fechar()


@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.fechar()
    sessao_obj.roll_back()
