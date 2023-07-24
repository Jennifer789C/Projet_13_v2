"""
Définit les modèles de l'application 'Lettings' qui seront affichés
sur le site Admin de ce projet.
"""
from django.contrib import admin
from .models import Letting
from .models import Address

admin.site.register(Letting)
admin.site.register(Address)
