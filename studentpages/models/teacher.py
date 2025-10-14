from django.db import models

class teacher(models.Model):
    fkuser = models.ForeignKey()
    name = models.TextField()
    surname = models.TextField()
    subjects = models.ManyToManyField('subject', related_name='teachers')
    
    def __str__(self):
        return f"{self.name} {self.surname}"

# profile - тип хотел профиль добавить к преподу, а нахер он нужен?