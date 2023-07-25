"""
Définit les fixtures de l'application 'Lettings'.
"""
from django.test import Client
import pytest
from lettings.models import Address, Letting


@pytest.fixture()
def client():
    """
    Définit le client pour tester les requêtes HTTP.

    :return : une instance du client fournit par django
    """
    client = Client()
    return client


@pytest.fixture()
def address():
    """
    Crée une adresse fictive.

    :return : une instance du :model: `letting.Address`
    """
    address = Address.objects.create(number=250,
                                     street="Main Street",
                                     city="New York City",
                                     state="NY",
                                     zip_code=85263,
                                     country_iso_code="USA")
    return address


@pytest.fixture()
def letting(address):
    """
    Crée un lieu de location fictif.

    :param address : reprend la fixture 'address'

    :return : une instance du :model: `letting.Letting`
    """
    letting = Letting.objects.create(title="Auberge du soleil",
                                     address_id=address.id)
    return letting
