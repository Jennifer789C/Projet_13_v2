"""
Définit le modèle de l'application 'Profiles' qui sera affiché
sur le site Admin de ce projet.
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
