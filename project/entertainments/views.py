from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EntertainmentsSerializer
import requests

from .models import Entertainments


class EntertainmentsViewSet(viewsets.ModelViewSet):
    queryset = Entertainments.objects.all()
    serializer_class = EntertainmentsSerializer


class EntertainmentsView(APIView):
    permission_classes = [AllowAny]
    serializer = EntertainmentsSerializer
    api_url = 'http://www.boredapi.com/api/activity'

    def post(self, request):
        response = requests.get(self.api_url)

        self.serializer.save_response(response.json(), response_data=response.json())

        return Response(status=response.status_code)
