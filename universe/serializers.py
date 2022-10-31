from rest_framework import serializers

from core.models import Character


class CharacterInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name']


class CharacterOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
