from django.urls import path

from .views import JokeView

urlpatterns = [
    path('joke/', JokeView.as_view(), name='joke'),
]
