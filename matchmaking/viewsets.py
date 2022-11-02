from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Request, Response

from .serializers import GameServerInstanceSerializer
from .models import GameServerInstance


class GameServerInstanceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = GameServerInstance.objects.all()
    serializer_class = GameServerInstanceSerializer


class GetGameServerInstanceView(APIView):

    def get(self, request: Request, format=None) -> Response:
        # TODO: needs better filtering based on request parameters
        game_server_instance = GameServerInstance.objects.first()
        if game_server_instance == None:
            # If there isnt any available game server instance running
            # Send a request to the GameServerManager to spawn one.
            # This is something specific thats why is not implemented here
            new_game_server_instance = GameServerInstance(
                ip='127.0.0.1', port=9090, max_players=20)
            new_game_server_instance.save()
            game_server_instance = new_game_server_instance

        sr = GameServerInstanceSerializer(game_server_instance)
        return Response(sr.data)
    pass
