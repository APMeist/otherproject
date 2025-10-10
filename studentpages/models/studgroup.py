from django.db import models

class studgroup(models.Model):
    groupname = models.TextField
    studingroup = models.ForeignKey