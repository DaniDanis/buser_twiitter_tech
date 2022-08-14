import pytest
from model_bakery import baker
from django.contrib.auth import get_user_model
from pagina_web.models import Posts
from pagina_web.views import tocomment


@pytest.fixture()
def user(db):
    User = get_user_model()
    return User.objects.create(username='test', email='test@test.com', password='teste')
    


@pytest.fixture()
def client_logged(client, user):
    client.force_login(user)
    return client

# teste de acesso a home com o usuario logado
def test_acess_home_logged(client_logged):
    response = client_logged.get('/home/')
    assert response.status_code == 200

# teste de acesso a home SEM usuario logado
def test_acess_home_not_logged(client):
    response = client.get('/home/')
    assert response.status_code == 302

# teste de criacao de post com usuario logado
def test_post_logged(client_logged, db):
    client_logged.post('/home', {
        'text-input': 'postSalvo',
    })
    Posts.objects.count == 1

# teste de criar post sem usuario logado
def test_post_not_logged(client, db):
    client.post('/home', {
        'text-input': 'postSalvo',
    })
    Posts.objects.count == 0

# teste de comentar post estando logado
def test_comment_logged(user, db, rf):
    post = baker.make(Posts)
    request = rf.post('/tocomment/', {
        "text-input": "CommentSalvo",
        'input-post-id': 1,
    })
    user.save()
    request.user = user
    request.META['HTTP_REFERER'] = '/home/'
    tocomment(request)
    assert Posts.objects.filter(is_comment = post).count() == 1


# teste de comentar post estando  NAO logado
def test_comment_not_logged(db, client):
    post = baker.make(Posts)
    client.post('/tocomment/', {
        "text-input": "CommentSalvo",
        'input-post-id': 1,
    })
    assert Posts.objects.filter(is_comment = post).count() == 0
    
    





