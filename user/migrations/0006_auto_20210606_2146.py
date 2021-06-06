# Generated by Django 3.2.4 on 2021-06-06 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_remove_worker_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='surname',
        ),
        migrations.AddField(
            model_name='client',
            name='full_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
