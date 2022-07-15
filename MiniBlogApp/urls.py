from django.urls import path, include


from .views import *

urlpatterns = [
     
    # URLS de ProyectoCoderApp
    path('', index, name="inicio"), # Vista de inicio de la app
    path('blog/', blog, name='blog'), # Vista de blogs
    path("login/", login_request, name="Login"),
    path("logout/", logout_request, name="LogOut"),
    path("register/", register, name="Register"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path('post/<int:id>/<slug:slug>', post_detail, name='post_detail') # Vista de template detallado de blogs, con id y slug unico asociado.
]