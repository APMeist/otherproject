from django.db import models

class Admin(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.login
