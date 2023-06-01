from rest_framework.response import Response
from rest_framework.decorators import api_view
from hltv.models import Player
from .serializers import PlayerSerializer
from rest_framework import viewsets


# #METODO GET
# @api_view(['GET'])
# def getData(request):
#     players = Player.objects.all()
#     serializer = PlayerSerializer(players, many=True)
#     return Response(serializer.data)
# #METODO POST
# @api_view(['POST'])
# def addPlayer(request):
#     serializer = PlayerSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    