# Generated by Django 3.2.4 on 2021-06-20 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lwt', '0009_myuser_is_subscribed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_subscribed',
        ),
    ]
