from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import JokeViewSet, JokeView

router = DefaultRouter()
router.register(r'standard_actions', JokeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('post_joke_from_api/', JokeView.as_view(), name='joke'),
]
