from django.urls import path

from . import views

app_name="hltv"

urlpatterns = [
    path('stats', views.stats, name='stats'),
    path('list_players', views.list_players, name='list_players'),
    path('noticias', views.noticias, name='noticias'),
    path('teams', views.teams, name='teams'),
    path('get_noticias', views.get_noticias, name='get_noticias'),
    path('get_teams', views.get_teams, name='get_teams'),
    #path('market', views.market, name='market'),
    #path('get_market', views.get_market, name='get_market'),
    
]


