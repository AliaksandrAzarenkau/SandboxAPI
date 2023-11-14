from random import randint

import requests
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import DogsPhoto
from .serializers import DogsPhotoSerializer
from django.conf import settings


class BaseDocumentPostView(APIView):
    permission_classes = [AllowAny]
    serializer_class = None
    api_url = None

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)

    def get(self, request):
        id_count = DogsPhoto.objects.count()
        response = DogsPhoto.objects.get(id=randint(1, id_count)).message
        return Response(response)


class DogsPhotoViewSet(viewsets.ModelViewSet):
    queryset = DogsPhoto.objects.all()
    serializer_class = DogsPhotoSerializer


class DogsPhotoView(BaseDocumentPostView, APIView):
    serializer_class = DogsPhotoSerializer
    api_url = settings.URL_PHOTOS



