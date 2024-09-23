from django.db import models
from django.contrib.auth.models import AbstractUser

#Definição do modelo de usuário personalizado
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def str(self):
        return self.username