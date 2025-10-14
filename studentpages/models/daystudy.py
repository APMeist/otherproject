from django.db import models


class daystudy(models.Model):
    firstlesson = models.ForeignKey('lesson')
    secondlesson = models.ForeignKey('lesson')
    thirdlesson = models.ForeignKey('lesson')
    fourthlesson = models.ForeignKey('lesson')
    fifthlesson = models.ForeignKey('lesson')
    sixthlesson = models.ForeignKey('lesson')
    seventhlesson = models.ForeignKey('lesson')
    datefield = models.DateField()
    
