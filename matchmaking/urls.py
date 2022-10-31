from rest_framework import routers

from .viewsets import GameServerInstanceViewSet

router = routers.DefaultRouter()
router.register(r'gameserverinstances', GameServerInstanceViewSet)

urlpatterns = router.urls
