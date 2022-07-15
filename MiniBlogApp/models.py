from django.db import models
from django.contrib.auth.models import User


<<<<<<< HEAD
=======
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    subject = models.CharField(max_length=255, blank=False)
    message = models.TextField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
>>>>>>> 2a1b38b098010972325ce498d1608cc0cf625009
