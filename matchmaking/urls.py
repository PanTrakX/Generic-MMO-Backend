from django.urls import path
from rest_framework import routers

from .viewsets import GameServerInstanceViewSet
from .viewsets import GetGameServerInstanceView

router = routers.DefaultRouter()
router.register(r'gameserverinstances', GameServerInstanceViewSet)

urlpatterns = [
    path('get_game_server_instance/', GetGameServerInstanceView.as_view())
]
urlpatterns += router.urls
