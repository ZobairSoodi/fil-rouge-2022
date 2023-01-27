# Generated by Django 4.0.5 on 2022-06-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameDB', '0005_remove_game_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='difficulty',
            name='game_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gameDB.game'),
            preserve_default=False,
        ),
    ]
