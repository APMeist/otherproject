from django.db import models

class daylist(models.Model):
    lesson = models.ForeignKey('lesson', on_delete=models.CASCADE, related_name='timetable_entries')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    class Meta:
        unique_together = ('date', 'start_time')

    def __str__(self):
        return f"{self.lesson.name} on {self.date} from {self.start_time} to {self.end_time}"