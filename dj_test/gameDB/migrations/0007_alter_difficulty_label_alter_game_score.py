# Generated by Django 4.0.4 on 2022-05-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameDB', '0006_alter_game_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='difficulty',
            name='label',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='game',
            name='score',
            field=models.IntegerField(),
        ),
    ]
