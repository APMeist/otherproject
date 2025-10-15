from django.db import models

class Studgroup(models.Model):
    groupname = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.groupname