from rest_framework import viewsets
from rest_framework.views import APIView, Request, Response
from rest_framework.authtoken.models import Token

from .serializers import GameServerInstanceSerializer
from .serializers import GameServerInstanceForPlayerSerializer
from .models import GameServerInstance


class GameServerInstanceViewSet(viewsets.ModelViewSet):
    queryset = GameServerInstance.objects.all()
    serializer_class = GameServerInstanceSerializer


class GetGameServerInstanceView(APIView):

    def get(self, request: Request, format=None) -> Response:
        # TODO: needs better filtering based on request parameters
        game_server_instance = GameServerInstance.objects.first()
        if game_server_instance == None:
            # If there isnt any available game server instance running
            # Send a request to the GameServerManager to spawn one.
            # passing the uuid as a server_auth_token and waiting for the response
            # to create a model instance
            # This is something specific thats why is not implemented here
            new_game_server_instance = GameServerInstance(
                is_staff=True,
                is_server=True,
                ip='127.0.0.1',
                port=9090,
                max_players=20)
            new_game_server_instance.save()
            token = Token.objects.get_or_create(
                user=new_game_server_instance)[0].key
            game_server_instance = new_game_server_instance

        sr = GameServerInstanceForPlayerSerializer(game_server_instance)
        return Response(sr.data)
