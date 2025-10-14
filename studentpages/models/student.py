from django.db import models

# Студент. Хочу понять как генерировать юньку. В юзерах - пассворд.


class student(models.Model):
    name = models.TextField()
    surname = models.TextField()
    uniquekey = models.CharField()
    group = models.CharField()
    course = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.surname}"