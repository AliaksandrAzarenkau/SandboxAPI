from random import randint

from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EntertainmentsSerializer
import requests

from .models import Entertainments
from django.conf import settings


class EntertainmentsViewSet(viewsets.ModelViewSet):
    queryset = Entertainments.objects.all()
    serializer_class = EntertainmentsSerializer


class EntertainmentsView(APIView):
    permission_classes = [AllowAny]
    serializer = EntertainmentsSerializer
    api_url = settings.URL_ENTERTAINMENTS

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer.save_response(response.json(), response_data=response.json())
        return Response(status=response.status_code)

    def get(self, request):
        id_count = Entertainments.objects.count()
        response_entertainment = Entertainments.objects.get(id=randint(1, id_count)).entertainment
        response_participants = Entertainments.objects.get(id=randint(1, id_count)).participants
        response_price = Entertainments.objects.get(id=randint(1, id_count)).price
        response_accessibility = Entertainments.objects.get(id=randint(1, id_count)).accessibility
        return Response({"entertainment": response_entertainment,
                         "participants": response_participants,
                         "price": response_price,
                         "accessibility": response_accessibility})
