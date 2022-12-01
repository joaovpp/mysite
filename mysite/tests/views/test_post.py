import pytest
import json

from django.urls import reverse


@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home') #ainda vamos criar essa pagina
    response = client.get(url)
    assert response.status_code == 200 #resultado esperado

    assert response.content == b'Hello World' #resultado esperado
