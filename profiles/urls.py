"""
Définit les points de terminaison de l'application 'Profiles'.
"""
from django.urls import path
from . import views

app_name = "profiles"
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/', views.profile, name='profile'),
]
