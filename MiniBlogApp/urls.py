from django import views
from django.urls import path, include


from .views import *

urlpatterns = [
     
    # URLS de ProyectoCoderApp
    path('', index, name="inicio"), # Vista de inicio de la app
    path('blog/', blog, name='blog'), # Vista de blogs
    path('post/<int:id>/<slug:slug>', post_detail, name='post_detail'), # Vista de template detallado de blogs, con id y slug unico asociado.
    path('contact/', contact, name='contacto'), # Vista de contacto ,
    path('about/', about, name='about' ),    # Vista de sobre nosotros ,
    path("login/", login_request, name="Login"),
    path("logout/", logout_request, name="LogOut"),
    path("register/", register, name="Register"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
]