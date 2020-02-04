
from django.db import models
from django.urls import reverse

from people.models import Lecturer


class Course(models.Model):
    GEOLOGY = '1'
    GEOPHYSICS = '2'
    OTHERS = '3'

    CATEGORIES = (
        (GEOLOGY, 'Geology'),
        (GEOPHYSICS, 'Geophysics'),
        (OTHERS, 'Others'),
    )

    title = models.CharField(max_length=400)
    code = models.CharField(max_length=6, unique=True)
    category = models.CharField(choices=CATEGORIES, max_length=2)
    units = models.PositiveIntegerField()
    description = models.TextField()
    drive_link = models.URLField(blank=True)
    lecturers = models.ManyToManyField(Lecturer, related_name='courses')

    def __str__(self):
        return self.code

    def verbose_category(self):
        return dict(self.CATEGORIES)[self.category]

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={
            'code': self.code.lower(),
            'category': dict(self.CATEGORIES)[self.category].lower(),
        })
