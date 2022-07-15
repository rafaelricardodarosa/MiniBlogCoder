from django.contrib import admin

from .models import *

# Registre sus modelos aquí para que sea posible visualizar via django admin
admin.site.register(Contact)
