import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/", default='images/default_profile_pic.png')


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Game(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    score = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now)
    duration = models.IntegerField(blank=True)
    won = models.BooleanField(default=False)


class Difficulty(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    label = models.CharField(max_length=10)
