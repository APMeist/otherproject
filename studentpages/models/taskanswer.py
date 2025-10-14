from django.db import models


#Ну тут домашка тип. Я хрен его знает, как мне еще сказать. Возможное создание запроса для того, чтобы выдать все.

class Taskanswer(models.Model):
    answerer = models.ForeignKey
    task = models.ForeignKey
    filesanswer = models.BinaryField