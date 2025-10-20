from django.db import models

class Teacher(models.Model):
    fkuser = models.ForeignKey('User', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    departments = models.ManyToManyField('Department', related_name='teachers')
    
    def __str__(self):
        return f"{self.name} {self.surname}"

# profile - тип хотел профиль добавить к преподу, а нахер он нужен?