from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .viewsets import CharactersViewSet


router = DefaultRouter()
router.register(r'characters', CharactersViewSet)

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]
urlpatterns += router.urls
