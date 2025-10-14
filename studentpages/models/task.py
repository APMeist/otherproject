from django.db import models

#тип тут надо попытаться сделать задание которое выдается всем группам. Это делать надо на беке!

class Task(models.Model):
    subject = models.ForeignKey
    teacher = models.ForeignKey
    studgroup = models.ForeignKey