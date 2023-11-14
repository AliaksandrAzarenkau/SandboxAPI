from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DogsPhotoViewSet, DogsPhotoView

router = DefaultRouter()
router.register(r'standard_actions', DogsPhotoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('dogs_foto/', DogsPhotoView.as_view(), name='dogs_foto'),
]
