
from django.urls import reverse
from django.utils.text import slugify
from django.db import models


def create_unique_slug(model, instance):
    expected_slug = slugify(instance.title)
    rivals = model.objects.filter(
        slug__startswith=expected_slug
    ).count()

    if rivals > 0:
        str_length = 100 - len(str(rivals))
        slug = '{}-{}'.format(
            expected_slug[:str_length - 1],
            rivals + 1
        )
    else:
        slug = expected_slug
    return slug


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/events/')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    ticket_price = models.FloatField(null=True, default=0.0)
    slug = models.SlugField(unique=True, blank=False)
    description = models.TextField()
    organisers = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.end_date:
            date = self.start_date
            self.end_date = date.replace(hour=20, minute=0)

        if not self.slug:
            self.slug = create_unique_slug(Event, self)
        super().save(*args, **kwargs)
