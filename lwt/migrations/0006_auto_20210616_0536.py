# Generated by Django 3.2.4 on 2021-06-16 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lwt', '0005_alter_words_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='texts',
            name='is_webpage',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='languages',
            name='exceptionssplitsentences',
            field=models.CharField(default='(?<=Mr)\\.|(?<=Dr)\\.|(?<=[A-Z])\\.|(?<=Vd)\\.|(?<=Vds)\\.', max_length=500),
        ),
    ]
