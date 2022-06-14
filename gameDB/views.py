from .models import Profile, Game, Difficulty
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


# Test view
def test(request):
    user = Profile.objects.filter(game__score__gt=0).order_by('-game__score').values('game__score')[:2]
    c = Profile.objects.filter(game__score__gt=99)
    return HttpResponse(user)


# Home view
def home_page(request):
    return render(request, 'gameDB/home.html')


# Main game view
@login_required
def game_page(request):
    return render(request, template_name='gameDB/index.html')


# Submit score view
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
