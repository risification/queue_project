# Generated by Django 3.2.4 on 2021-06-07 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_book_client', '0003_tobookclient_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tobookclient',
            name='worker',
        ),
    ]
