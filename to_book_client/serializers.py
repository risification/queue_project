from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from .models import ToBookClient
from user.serializers import WorkerSerializer


class ToBookClientSerializers(serializers.ModelSerializer):
    worker_set = WorkerSerializer(many=True)

    class Meta:
        model = ToBookClient
        fields = ['id', 'client', 'time_to_book', 'worker_set']
