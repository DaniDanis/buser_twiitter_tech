from contas import urls
from django import urls
import pytest
from django.contrib.auth import get_user_model


# testa se as páginas de registro enstão realmente sendo renderizadas
@pytest.mark.parametrize('param', [
    ('opcoes'),
    ('registro'),
    ('login'),
])
def test_renderizar_views_login(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


def test_registro_usuario(client, user_data, db):
    User = get_user_model()
    assert User.objects.count() == 0
    registro_url = urls.reverse('registro')
    resp = client.post(registro_url, user_data)
    assert User.objects.count() == 1
    assert resp.satus_code == 302
