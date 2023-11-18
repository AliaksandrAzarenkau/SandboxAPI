from django.urls import path

from .views import DogsPhotoView

urlpatterns = [
    path('dogs_foto/', DogsPhotoView.as_view(), name='dogs_foto'),
]
