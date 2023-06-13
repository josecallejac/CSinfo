from rest_framework import serializers
from hltv.models import Player, Noticias, Teams, Market


class PlayerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Player
        fields = '__all__'

class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'


