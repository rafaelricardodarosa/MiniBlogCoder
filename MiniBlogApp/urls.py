from django import views
from django.urls import path, include


from .views import *

urlpatterns = [
     
    # URLS de ProyectoCoderApp
    path('', index, name="inicio"), # Vista de inicio de la app
    path('blog/', blog, name='blog'), # Vista de blogs
    path('post/<int:id>/<slug:slug>', post_detail, name='post_detail'), # Vista de template detallado de blogs, con id y slug unico asociado.
    path('contact/', contact, name='contacto'), # Vista de contacto ,
    path('about/', about, name='about' ), # Vista de sobre nosotros ,
    
]