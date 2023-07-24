"""
Définit les modèles de l'application 'Profiles'.

Cette application est composée d'un modèle :
- Profile, représentant un utilisateur
"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Cette classe représente un profil utilisateur.

    Elle est constituée de :
    user : relation un-à-un avec le modèle 'User' par défaut de django
    favorite_city : texte d'une longueur maximale de 64 caractères
                    correspondant à la ville favorite de l'utilisateur
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    class Meta:
        """
        Une métaclasse définissant le pluriel du modèle.
        """
        verbose_name_plural = "Profiles"

    def __str__(self):
        """
        Une fonction string représentant le modèle en texte.

        :return : le nom d'utilisateur
        """
        return self.user.username
