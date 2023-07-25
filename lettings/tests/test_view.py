"""
Répertorie les tests concernant les vues de l'application 'Lettings'.
"""
from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_view_letting_index(client, letting):
    """
    Teste la vue index
    :param client : reprend la fixture client
    :param letting : reprend la fixture letting
    """
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assert b'<title>Lettings</title>' in response.content
    assert letting in response.context["lettings_list"]


@pytest.mark.django_db
def test_view_letting(client, letting):
    """
    Teste la vue letting
    :param client : reprend la fixture client
    :param letting : reprend la fixture letting
    """
    response = client.get(reverse("lettings:letting", args=[f"{letting.id}"]))
    assert response.status_code == 200
    assert letting.title == "Auberge du soleil"
    assert b'<title>Auberge du soleil</title>' in response.content
    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address
