from django.db import models

class teacher(models.Model):
    fkuser = models.ForeignKey()
    name = models.TextField()
    surname = models.TextField()
    
    
    

# profile - тип хотел профиль добавить к преподу, а нахер он нужен?