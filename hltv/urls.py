from django.urls import path

from . import views

app_name="hltv"

urlpatterns = [
    #path('players', views.players, name='players'),
    path('stats', views.stats, name='stats'),
    path('noticias', views.noticias, name='noticias'),
    
]


