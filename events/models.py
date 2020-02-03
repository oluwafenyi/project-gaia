
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/events/', blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    ticket_price = models.FloatField(null=True, default=0.0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.end_date:
            date = self.start_date
            self.end_date = date.replace(hour=20, minute=0)
        super().save(*args, **kwargs)
