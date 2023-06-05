from django.shortcuts import render, redirect
from django.http import HttpResponse
from hltv.models import Player, Noticias
import requests

from django.conf import settings

# Create your views here.

#def players(request):
#    #pull data from third party rest api
#    response = requests.get('https://hltv-api.vercel.app/api/player.json')
#    #convert reponse data into json
#    players = response.json()
#    print(players)
#    return render(request, "pages/hltv.html", {'players': players})
#    pass


def stats(request):
    nickname = request.GET.get('nickname')
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    jugadores = Player.objects.all()
    return render(request, 'pages/stats.html', {'jugadores': jugadores})


def noticias(request):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    noticias = Noticias.objects.all()
    return render(request, 'pages/noticias.html', {'noticias': noticias} )







