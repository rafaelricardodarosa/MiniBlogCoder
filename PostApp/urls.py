from django.urls import path, include


from .views import *

urlpatterns = [
     
    # URLS de ProyectoCoderApp
    path('', post, name="post"), #vista de inicio de la app
    
]