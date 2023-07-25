"""
Répertorie les tests concernant les points de terminaison de l'application 'Profiles'.
"""
from django.urls import reverse, resolve
from profiles.views import index, profile


def test_url_profile_index():
    """
    Teste la vue utilisée à partir de :url: `profiles:index`
    """
    url = reverse("profiles:index")
    assert resolve(url).view_name == "profiles:index"
    assert resolve(url).func == index


def test_url_profile():
    """
    Teste la vue utilisée à partir de :url: `profiles:profile`
    """
    url = reverse("profiles:profile", args=[1])
    assert resolve(url).view_name == "profiles:profile"
    assert resolve(url).func == profile
