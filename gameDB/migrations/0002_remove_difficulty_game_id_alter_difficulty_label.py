# Generated by Django 4.0.5 on 2022-06-18 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameDB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='difficulty',
            name='game_id',
        ),
        migrations.AlterField(
            model_name='difficulty',
            name='label',
            field=models.CharField(default='Easy', max_length=10),
        ),
    ]
