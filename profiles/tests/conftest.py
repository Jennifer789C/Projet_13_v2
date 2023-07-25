"""
Définit les fixtures de l'application 'Profiles'.
"""
from django.contrib.auth import get_user_model
from django.test import Client
import pytest
from profiles.models import Profile

User = get_user_model()


@pytest.fixture()
def client():
    """
    Définit le client pour tester les requêtes HTTP.

    :return : une instance du client fournit par django
    """
    client = Client()
    return client


@pytest.fixture()
def profile():
    """
    Crée un profil utilisateur fictif.

    :return : une instance du :model: `profiles.Profile`
    """
    user = User.objects.create(password="mdp",
                               username="test")
    profile = Profile.objects.create(user_id=user.id,
                                     favorite_city="Brooklynn")
    return profile
