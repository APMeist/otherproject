from django.db import models

#тип тут надо попытаться сделать задание которое выдается всем группам. Это делать надо на беке!

class Task(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    studgroup = models.ForeignKey('Studgroup', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateTimeField()
    task = models.FileField(upload_to='tasks/')

    def __str__(self):
        return self.title