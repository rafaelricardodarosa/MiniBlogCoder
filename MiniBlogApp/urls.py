from django.urls import path, include


from .views import *

urlpatterns = [
     
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"), #vista de inicio de la app
    
]