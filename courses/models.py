
from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=400)
    code = models.CharField(max_length=5, unique=True)
    units = models.PositiveIntegerField()
    description = models.TextField()
    drive_link = models.URLField()

    def __str__(self):
        return self.code
