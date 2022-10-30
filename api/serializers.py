from dataclasses import fields
from rest_framework import serializers

from core.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
