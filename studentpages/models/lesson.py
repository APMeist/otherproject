from django.db import models

class lesson(models.Model):
    subject = models.ForeignKey('subject', on_delete=models.CASCADE, related_name='lesson')
    teacher = models.ForeignKey('teacher', on_delete=models.CASCADE, related_name='lesson')
    name = models.CharField(max_length=100)



