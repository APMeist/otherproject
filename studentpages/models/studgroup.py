from django.db import models

class Studgroup(models.Model):
    groupname = models.TextField
    studingroup = models.ForeignKey