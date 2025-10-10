from django.db import models

#Юзер. Тут пограничим всякое.


class user(models.Model):
    login = models.TextField()
    password = models.TextField()
