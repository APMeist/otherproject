from django.db import models
from django.contrib.auth.models import AbstractUser

class Admin(AbstractUser):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.login
