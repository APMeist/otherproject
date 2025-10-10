from django.db import models

# тут должна быть модель для портфолио. По факту оно вот такое тип. 

class portfolio(models.Model):
    fileportfolio = models.BinaryField
    description = models.CharField
    studentportowner = models.ForeignKey