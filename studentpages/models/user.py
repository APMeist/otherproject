from django.db import models
#Юзер. Тут пограничим всякое.


class User(models.Model):
    uslog = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.log
