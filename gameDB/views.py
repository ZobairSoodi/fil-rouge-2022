import json

from .models import Profile, Game, Difficulty
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
    return render(request, template_name='gameDB/index.html')


def store_data(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        profile = request.POST.get('profile')
        duration = request.POST.get('duration')
        won = request.POST.get('won')
        difficulty = request.POST.get('difficulty')
        newGame = Game(
                       profile_id=Profile.objects.get(user_id=profile),
                       score=score,
                       duration=duration,
                       won=won
                       )
        newGame.save()
        newDifficulty = Difficulty(
            game_id=newGame,
            label=difficulty
        )
        newDifficulty.save()
    return redirect('game')


def base(request):
    return render(request, template_name='gameDB/base.html')


def paddle(request):
    return render(request, template_name='gameDB/paddle_game.html')
