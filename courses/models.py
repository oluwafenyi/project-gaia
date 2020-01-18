
from django.db import models


class Course(models.Model):
    GEOLOGY = 1
    GEOPHYSICS = 2
    OTHERS = 3

    CATEGORIES = (
        (GEOLOGY, 'Geology'),
        (GEOPHYSICS, 'Geophysics'),
        (OTHERS, 'Others'),
    )

    title = models.CharField(max_length=400)
    code = models.CharField(max_length=5, unique=True)
    category = models.CharField(choices=CATEGORIES, max_length=2)
    units = models.PositiveIntegerField()
    description = models.TextField()
    drive_link = models.URLField()

    def __str__(self):
        return self.code
