import json

from .models import Profile, Game
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.templatetags.static import static

# Create your views here.


def home_page(request):
    test = Profile.objects.get(profile_pic='images/default_profile_pic.png')
    media_url = settings.MEDIA_URL
    return HttpResponse("<img src='" + media_url + str(test.profile_pic) + "' />")


def game_page(request):
    return render(request, template_name='gameDB/game/phaser/index.html')


def store_data(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        profile = request.POST.get('profile')
        duration = request.POST.get('duration')
        newGame = Game(profile_id=Profile.objects.get(user_id=profile), score=score, duration=duration)
        newGame.save()
    return redirect('game')
