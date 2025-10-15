from django.db import models

# Студент. Хочу понять как генерировать юньку. В юзерах - пассворд.


class Student(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    uniquekey = models.CharField(unique=True, max_length=20)
    group = models.ForeignKey('Studgroup', on_delete=models.CASCADE)
    course = models.IntegerField()
    
    def __str__(self):
        return f"{self.name} {self.surname}"