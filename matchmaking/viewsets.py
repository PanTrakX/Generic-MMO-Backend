from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

from .serializers import GameServerInstanceSerializer
from .models import GameServerInstance


class GameServerInstanceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser, IsAuthenticatedOrReadOnly]
    queryset = GameServerInstance.objects.all()
    serializer_class = GameServerInstanceSerializer
