from django.db import models
from user.models import Worker, Client


# Create your models here.


class ToBookClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    time_to_book = models.DateTimeField()
