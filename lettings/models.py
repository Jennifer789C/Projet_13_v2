"""
Définit les modèles de l'application 'Lettings'.

Cette application est composée de 2 modèles :
- Address, représentant une adresse postale
- Letting, représentant un lieu de location
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Cette classe représente une adresse postale.

    Elle est constituée de :
    number : nombre entier positif inférieur à 9 999 correspondant au numéro de la rue
    street : texte d'une longueur maximale de 64 caractères correspondant au nom de la rue
    city : texte d'une longueur maximale de 64 caractères correspondant au nom de la ville
    state : texte d'une longueur de 2 caractères correspondant à l'acronyme de l'Etat
    zip_code : nombre entier positif inférieur à 99 999 correspondant au code postal
    country_iso_code : texte d'une longueur de 3 caractères correspondant au code ISO du pays
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """
        Une métaclasse définissant le pluriel du modèle.
        """
        verbose_name_plural = "Addresses"

    def __str__(self):
        """
        Une fonction string représentant le modèle en texte.

        :return : le numéro et la rue du modèle
        """
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """
    Cette classe représente un lieu de location.

    Elle est constituée de :
    title : texte d'une longueur maximale de 256 caractères correspondant au titre de la location
    address : relation un-à-un avec le modèle 'Address'
    """
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        """
        Une métaclasse définissant le pluriel du modèle.
        """
        verbose_name_plural = "Lettings"

    def __str__(self):
        """
        Une fonction string représentant le modèle en texte.

        :return : le titre du modèle
        """
        return self.title
