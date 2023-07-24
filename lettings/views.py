"""
Définit les vues de l'application 'Lettings'.

Cette application est composée de 2 vues :
- index, listant tous les lieux de location
- letting, précisant les détails d'un lieu de location précis
"""
from django.shortcuts import render
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id
# arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices
# posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Cette vue affiche une liste de tous les lieux de location

    **Contexte**
    Liste de toutes les instances du :model:`lettings.Letting`

    **Gabarit**
    :template:`lettings/index.html`
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan
# porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus
# urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean finibus
# faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim
# mattis enim, ac condimentum velit libero in magna. Suspendisse potenti. In
# tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In
# tristique mauris eu velit fermentum, tempus pharetra est luctus. Vivamus
# consequat aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris
# condimentum auctor elementum. Donec quis nisi ligula. Integer vehicula
# tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Cette vue affiche les détails d'un lieu de location.

    **Contexte**
    Une instance de :model:`letting.Letting`

    **Gabarit**
    :template:`lettings/letting.html`
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
