from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Character
from universe.serializers import CharacterOutputSerializer, CharacterInputSerializer


class CharactersViewSet(viewsets.ModelViewSet):
    """
    Get: List/Retrieve all the owned character by the user from the request
    Post: Create a character
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Character.objects.all()

    def get_queryset(self):
        """
        Get only the instances that are owned by the user
        """
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user)
        return query_set

    def get_serializer_class(self):
        """
        Get different serializers based on the action input/output
        """
        if self.action == 'create' or self.action == 'update':
            return CharacterInputSerializer
        return CharacterOutputSerializer

    def perform_create(self, serializer):
        """
        Fill the user field of the Character instance with the user from the request
        """
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)
