from rest_framework import serializers

from .models import GameServerInstance


class GameServerInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameServerInstance
        fields = '__all__'
