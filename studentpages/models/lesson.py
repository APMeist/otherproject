from django.db import models

class Lesson(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='lesson')
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, related_name='lesson')
    name = models.CharField(max_length=100)
    group = models.ForeignKey('Studgroup', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



