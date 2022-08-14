import pytest
from django.contrib.auth.models import User, AnonymousUser
from model_bakery import baker
from pagina_web.views import home, tocomment
from pagina_web.models import Posts


url_rf_logged = ''
data_post_logged = {}

@pytest.fixture
def user_for_login(db):
    return baker.make(User)

# Retorna um request para home já logada
@pytest.fixture
def request_get_logged(rf, user_for_login):
    request =  rf.get(url_rf_logged)
    request.user = user_for_login
    return request

@pytest.fixture
def request_post_logged(rf, user_for_login):
    request = rf.post(url_rf_logged, data_post_logged)
    request.user = user_for_login
    return request

# test o acesso à home com o usuário logado
def test_logged(request_get_logged):
    url_rf_logged = "/home/"
    response = home(request_get_logged)
    assert response.status_code == 200

# test o acesso à home com o usuário não autenticado
def test_not_authenticated(rf):
    request = rf.get("/home/")
    request.user = AnonymousUser()
    response = home(request)
    assert response.status_code == 302

# testa fazer posts quando logado
def test_post_logged_(request_post_logged, rf,db, user_for_login):
    request = rf.post('/home/', {
        'text-input': 'aaaaaaaaaaaaa',
    })
    request.user = user_for_login
    home(request)
    assert Posts.objects.count() == 1


# testa fazer posts quando nao logado
def test_post_not_logged(rf, db ):
    request = rf.post('/home/', {
        'text-input': 'aaaaaaaaaaaaa',
    })
    request.user = AnonymousUser()
    home(request)
    assert Posts.objects.count() == 0


   


    








