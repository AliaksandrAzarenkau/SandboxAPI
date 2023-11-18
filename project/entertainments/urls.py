from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import EntertainmentsViewSet

router = DefaultRouter()
router.register(r'standard_actions', EntertainmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('entertainments/', views.EntertainmentsView.as_view(), name='entertainments'),
]