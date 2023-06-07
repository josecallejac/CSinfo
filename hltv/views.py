from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from hltv.models import Player, Noticias, Teams
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


#def stats(request):
#    nickname = request.GET.get('nickname')
#    if not request.user.is_authenticated:
#        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
#    jugadores = Player.objects.all()
#    return render(request, 'pages/stats.html', {'jugadores': jugadores})

# STATS DE JUGADORES
def stats(request):
    return render(request, 'pages/stats.html')

def list_players(request):
    players = list(Player.objects.values())
    data = {'players': players}
    return JsonResponse(data)

#NOTICIAS CSGO
def get_noticias(_request):
    noticias = list(Noticias.objects.values())
    if (len(noticias)>0):
        data={'message': "Success", 'noticias': noticias }
    else:
        data = {'message': 'NotFound'}
    return JsonResponse(data)

    

def noticias(request):
    #if not request.user.is_authenticated:
        #return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    #noticias = Noticias.objects.all()
    #return render(request, 'pages/noticias.html', {'noticias': noticias} )
    return render(request, 'pages/noticias.html')


def team(request):
    team = Teams.objects.all()
    return render(request, 'pages/teams.html', {'team': team } )
    






