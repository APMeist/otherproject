from django.db import models


#Ну тут домашка тип. Я хрен его знает, как мне еще сказать. Возможное создание запроса для того, чтобы выдать все.

class Taskanswer(models.Model):
    answerer = models.ForeignKey('Student', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    filesanswer = models.BinaryField()
    mark = models.IntegerField()