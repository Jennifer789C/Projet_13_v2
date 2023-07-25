"""
Répertorie les tests concernant les points de terminaison du projet.
"""
from django.urls import reverse, resolve
from oc_lettings_site.views import index


def test_url_index():
    """
    Teste la vue utilisée à partir de :url: `index`
    """
    url = reverse("index")
    assert resolve(url).view_name == "index"
    assert resolve(url).func == index
