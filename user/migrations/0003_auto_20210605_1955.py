# Generated by Django 3.2.4 on 2021-06-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_client_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='full_name',
        ),
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='surname',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
