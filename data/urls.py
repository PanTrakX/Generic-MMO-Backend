from rest_framework.routers import DefaultRouter

from data.viewsets import CharactersViewSet


router = DefaultRouter()
router.register(r'characters', CharactersViewSet, basename='Characters')

urlpatterns = router.urls
