from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Character
from data.serializers import CharacterOutputSerializer, CharacterInputSerializer


class CharactersViewSet(viewsets.ModelViewSet):
    """
    This is supposed the be created by the user/player as it is GameServer independent
    The player will create a character before joining any GameServer 
    Only the server can update the character to add things like XP
    Get: List/Retrieve all the owned character by the user from the request
    Post: Create a character
    """
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """
        If user is_staff get all the characters
        Is user is not staff get only the owned characters
        """
        if not self.request.user.is_staff:
            self.queryset = Character.objects.filter(user=self.request.user)
        return Character.objects.all()

    def get_serializer_class(self):
        """
        Get different serializers based on the action input/output
        """
        if self.action == 'create' or self.action == 'update':
            return CharacterInputSerializer
        return CharacterOutputSerializer

    def get_permissions(self):
        if self.action == 'create' or self.action == 'delete':
            return [IsAuthenticated()]
        elif self.action == 'update':
            return [IsAdminUser()]
        else:
            return [IsAdminUser(), IsAuthenticated()]

    def perform_create(self, serializer):
        """
        Performed by the user
        Fill the user field of the Character instance with the user from the request
        """
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

    def perform_update(self, serializer):

        return super().perform_update(serializer)
