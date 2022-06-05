from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_page, name='home'),
    path('game/', views.game_page, name='game'),
    path('storeData/', views.store_data, name='store-data'),
]