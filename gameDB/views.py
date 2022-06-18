from .models import Profile, Game, Difficulty
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Max, Count

# Create your views here.


# Home view
def home_page(request):
    return render(request, 'gameDB/home.html')


# How to play view
def how_to(request):
    return render(request, 'gameDB/how_to_play.html')


# Main game view
@login_required
def game_page(request):
    return render(request, template_name='gameDB/index.html')


# Submit score view
def store_data(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        profile_ = request.POST.get('profile')
        duration = request.POST.get('duration')
        won_ = request.POST.get('won')
        if won_ == "True":
            won = True
        else:
            won = False

        difficulty = request.POST.get('difficulty')
        newGame = Game(
                       profile_id=Profile.objects.get(user_id=profile_),
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


# Profile view
@login_required()
def profile(request):
    data = Profile.objects.filter(user__username=request.user.username).\
        order_by('-game__score').\
        values('user__username', 'game__difficulty__label',
               'game__score', 'game__won', 'game__date',
               'game__duration')

    profile_info = Profile.objects.filter(user__username=request.user.username).\
        aggregate(max_score=Max('game__score'))

    # games = Profile.objects.filter(user__username=request.user.username).\
    #     annotate(game_count=Count("game__score"),
    #              game_won=Count("game__won"))

    games_num = Game.objects.filter(profile_id__user__username=request.user.username).count()

    games_won = Game.objects.filter(profile_id__user__username=request.user.username, won=True).count()

    games_lost = Game.objects.filter(profile_id__user__username=request.user.username, won=False).count()

    return render(request=request,
                  template_name='gameDB/profile.html',
                  context={
                            'data': data,
                            'info': profile_info,
                            'games_num': games_num,
                            'games_won': games_won,
                            'games_lost': games_lost,
                          })


# High score view
def highscore(request):
    data = Profile.objects.filter(game__score__gt=0).order_by('-game__score').values('game__score', 'user__username').aggregate(Max('game__score'))
    return render(request=request, template_name='gameDB/highscore.html', context={'data': data})


# Base template view
def base(request):
    return render(request, template_name='gameDB/base.html')


# Paddle game view
def paddle(request):
    return render(request, template_name='gameDB/paddle_game.html')


# Sign Up view
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')
    else:
        form = SignUpForm()
    return render(request, 'gameDB/sign_up.html', {'form': form})


# Sign In view
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('game')
    return render(request, 'gameDB/sign_in.html')


# Log out view
@login_required
def log_out(request):
    logout(request)
    return redirect('sign-in')
