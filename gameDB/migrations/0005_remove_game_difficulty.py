# Generated by Django 4.0.5 on 2022-06-18 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameDB', '0004_alter_game_difficulty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='difficulty',
        ),
    ]
