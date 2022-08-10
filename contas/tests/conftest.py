import pytest

@pytest.fixture
def user_data():
    return {
        'nome': 'usuario',
        'sobrenome': 'silva',
        'email': 'usuario@email.com',
        'usuario': 'apelido_usuario',
        'senha': 'pass_321123',
        'senha2': 'pass_123321',
    }