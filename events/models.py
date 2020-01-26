
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)
    ticket_price = models.PositiveIntegerField(null=True)
