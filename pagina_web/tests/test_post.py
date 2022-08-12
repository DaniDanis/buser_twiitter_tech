from urllib import response
import pytest
from django.contrib.auth.models import User, AnonymousUser
from model_bakery import baker
from pagina_web.views import home, tocomment

# Url usada para os diferentes requests logados
url_rf_loged = ''

# fixture retorna um usuario salvo no banco
@pytest.fixture
def user_for_login(db):
    return baker.make(User)

# Retorna um request para home já logada
@pytest.fixture
def request_loged(rf, user_for_login):
    request =  rf.get(url_rf_loged)
    request.user = user_for_login
    return request

# test o acesso à home com o usuário logado
def test_loged(request_loged):
    url_rf_loged = "/home/"
    response = home(request_loged)
    assert response.status_code == 200

# test o acesso à home com o usuário não autenticado
def test_not_authenticated(rf):
    request = rf.get("/home/")
    request.user = AnonymousUser()
    response = home(request)
    assert response.status_code == 302

# def test_post(rf,db, user_for_login):
#     request = rf.post('/tocomment/', {
#         'user': user_for_login,
#         'POST': {'text-input': 'aaaaaaaaaaaaa'}
#     })
   


    








