# Generated by Django 3.2.4 on 2021-06-07 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_worker_to_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('working', 'working'), ("don't working", "don't working")], default=1, max_length=20),
            preserve_default=False,
        ),
    ]