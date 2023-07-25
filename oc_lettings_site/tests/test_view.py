"""
Répertorie les tests concernant les vues de l'application 'oc_lettings_site'.
"""
from django.urls import reverse
from django.test import Client
import pytest


@pytest.mark.django_db
def test_view_index():
    client = Client()
    response = client.get(reverse("index"))
    assert response.status_code == 200
    assert b'<title>Holiday Homes</title>' in response.content
