from django.db import models

class Daylist(models.Model):
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='timetable_entries')

    def __str__(self):
        return self.lesson.name