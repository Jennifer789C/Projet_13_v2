"""
Définit les vues de l'application 'Profiles'.

Cette application est composée de 2 vues :
- index, listant tous les profils utilisateurs
- profile, précisant les détails d'un profil utilisateur
"""
from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed
# consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Cette vue affiche une liste de tous les profils utilisateur

    **Contexte**
    Liste de toutes les instances du :model:`profiles.Profile`

    **Gabarit**
    :template:`profiles/index.html`
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque
# quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam
# dignissim congue. Pellentesque habitant morbi tristique senectus et netus et
# males
def profile(request, username):
    """
    Cette vue affiche les détails d'un profil utilisateur.

    **Contexte**
    Une instance de :model:`profiles.Profile`

    **Gabarit**
    :template:`profiles/profile.html`
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
