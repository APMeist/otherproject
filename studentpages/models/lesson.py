from django.db import models

class lesson(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    teacher = models.ForeignKey('teacher', on_delete=models.CASCADE)