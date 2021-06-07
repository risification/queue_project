from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)


class Worker(models.Model):
    full_name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(choices=(
        ('active', 'active'),
        ('working', 'working'),
        ("don't working", "don't working")
    ), max_length=20)
    phone = models.IntegerField()
