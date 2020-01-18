
from django.db import models

from courses.models import Course


class Person(models.Model):
    title = models.CharField(max_length=5, default='', blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '{}. {} {}'.format(self.title, self.first_name, self.last_name)

    def clean_title(self):
        return self.cleaned_data['title'].replace('.', '').title()

    class Meta:
        abstract = True


class Executive(Person):
    position = models.CharField(max_length=200)


class Lecturer(Person):
    courses = models.ManyToManyField(Course, related_name='lecturers')
