from rest_framework.routers import DefaultRouter

from universe.viewsets import CharactersViewSet


router = DefaultRouter()
router.register(r'characters', CharactersViewSet)

urlpatterns = router.urls
