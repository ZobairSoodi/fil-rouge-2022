from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('how_to/', views.how_to, name='how-to'),
    path('game/', views.game_page, name='game'),
    path('storeData/', views.store_data, name='store-data'),
    path('base/', views.base, name='base'),
    path('paddle/', views.paddle, name='paddle-game'),
    path('signup/', views.sign_up, name='sign-up'),
    path('signin/', views.sign_in, name='sign-in'),
    path('logout/', views.log_out, name='log-out'),
    path('profile/', views.profile, name='profile'),
    path('highscore/', views.highscore, name='highscore'),
]
