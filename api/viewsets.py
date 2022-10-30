from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Character
from api.serializers import CharacterSerializer


class CharactersViewSet(viewsets.ModelViewSet):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set
