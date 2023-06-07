from django.urls import path

from . import views

app_name="hltv"

urlpatterns = [
    path('stats', views.stats, name='stats'),
    path('list_players', views.list_players, name='list_players'),
    path('noticias', views.noticias, name='noticias'),
    path('team', views.team, name='team'),
    path('get_noticias', views.get_noticias, name='get_noticias'),
    
]


