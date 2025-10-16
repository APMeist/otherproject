from django.db import models

# тут должна быть модель для портфолио. По факту оно вот такое тип. 

class Portfolio(models.Model):
    name = models.CharField(max_length=70)
    fileportfolio = models.BinaryField()
    description = models.TextField()
    studentportowner = models.ForeignKey('Student', related_name='portfolio',
                                         default=None,  on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} on {self.studentportowner.name}"