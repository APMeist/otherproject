from django.db import models

class Teacher(models.Model):
    fkuser = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.TextField()
    surname = models.TextField()
    subjects = models.ManyToManyField('Subject', related_name='teachers')
    
    def __str__(self):
        return f"{self.name} {self.surname}"

# profile - тип хотел профиль добавить к преподу, а нахер он нужен?