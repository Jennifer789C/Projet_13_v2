"""
Définit les points de terminaison de tout le projet.
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls")),
    path('profiles/', include("profiles.urls")),
    path('admin/', admin.site.urls),
]
