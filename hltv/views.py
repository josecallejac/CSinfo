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

def list_players(_request):
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
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    #noticias = Noticias.objects.all()
    #return render(request, 'pages/noticias.html', {'noticias': noticias} )
    return render(request, 'pages/noticias.html')

""" #MARKET CSGO
def get_market(_request):
    market = list(Market.objects.values())
    if (len(market)>0):
        data={'message': "Success", 'market': market }
    else:
        data = {'message': 'NotFound'}
    return JsonResponse(data)

def market(request):
    #if not request.user.is_authenticated:
        #return redirect(f"{settings.LOGIN_URL}?next={request.path}")
    #noticias = Noticias.objects.all()
    #return render(request, 'pages/noticias.html', {'noticias': noticias} )
    return render(request, 'pages/market.html')
 """





#TEAMS CSGO
def get_teams(_request):
    teams = list(Teams.objects.values()) 
    if (len(teams)>0):
        data={'message': "Success", 'teams': teams }
    else:
        data = {'message': 'NotFound'}
    return JsonResponse(data)

def teams(request):    
    return render(request, 'pages/teams.html' )
    






