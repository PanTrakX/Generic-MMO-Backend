from rest_framework import serializers

from .models import Character


class CharacterInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name']


class CharacterOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
