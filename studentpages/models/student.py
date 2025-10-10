from django.db import models

# Студент. Хочу понять как генерировать юньку. В юзерах - пассворд.


class student(models.Model):
    uniquekey = models.CharField()
    group = models.CharField()
    course = models.IntegerField()
    
