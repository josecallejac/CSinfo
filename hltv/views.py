from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def players(request):
    #pull data from third party rest api
    response = requests.get('https://hltv-api.vercel.app/api/player.json')
    #convert reponse data into json
    players = response.json()
    print(players)
    return render(request, "pages/hltv.html", {'players': players})
    pass


