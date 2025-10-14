from django.db import models

#Юзер. Тут пограничим всякое.


class User(models.Model):
    login = models.TextField()
    password = models.TextField()
