"""
Répertorie les tests concernant les points de terminaison de l'application 'Lettings'.
"""
from django.urls import reverse, resolve
from lettings.views import index, letting


def test_url_letting_index():
    """
    Teste la vue utilisée à partir de :url: `lettings:index`
    """
    url = reverse("lettings:index")
    assert resolve(url).view_name == "lettings:index"
    assert resolve(url).func == index


def test_url_letting():
    """
    Teste la vue utilisée à partir de :url: `lettings:letting`
    """
    url = reverse("lettings:letting", args=[1])
    assert resolve(url).view_name == "lettings:letting"
    assert resolve(url).func == letting
