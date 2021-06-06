from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework import serializers
from .models import *
from .serviced import validate_password, mailing


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'phone', 'user']


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'full_name', 'phone', 'email', 'to_book', 'user']


class RegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(choices=(
        ('user', 'user'),
        ('worker', 'worker')
    ), write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'check_password', 'user_type']

    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password')
        check_password = validated_data.pop('check_password')
        user_type = validated_data.pop('user_type')
        if password != check_password:
            raise ValidationError("Password don't match")
        if validate_password(password):
            raise ValidationError("пароль должен состоят только из букв и цифр")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        if user_type == 'worker':
            user.is_active = False
            group = Group.objects.get(name='workers')
            user.groups.add(group)
            mailing(user.username)
        user.save()
        return user
