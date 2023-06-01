from rest_framework import serializers
from hltv.models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Player
        fields = '__all__'