
from django.db import models


class Person(models.Model):
    title = models.CharField(max_length=5, default='', blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/people/', blank=True)

    def __str__(self):
        return self.full_name()

    def full_name(self):
        if self.title:
            return '{}. {} {}'.format(
                self.title, self.first_name, self.last_name
            )
        return '{} {}'.format(self.first_name, self.last_name).strip()

    class Meta:
        abstract = True


class Executive(Person):
    position = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=11, blank=True)
    twitter = models.CharField(max_length=15, blank=True)
    instagram = models.CharField(max_length=30, blank=True)
    snapchat = models.CharField(max_length=15, blank=True)

    def whatsapp_link(self):
        if self.whatsapp:
            return 'https://wa.me/234{}'.format(self.whatsapp[1:])
        return None

    def snapchat_link(self):
        if self.snapchat:
            return 'https://snapchat.com/add/{}'.format(self.snapchat)
        return None


class Lecturer(Person):
    ...
