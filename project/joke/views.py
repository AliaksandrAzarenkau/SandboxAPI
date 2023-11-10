import requests
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Joke
from .serializers import JokeSerializer


class BaseDocumentPostView(APIView):
    permission_classes = [AllowAny]
    serializer_class = None
    api_url = None

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)


class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class JokeView(BaseDocumentPostView, APIView):
    # permission_classes = [AllowAny]
    serializer_class = JokeSerializer
    api_url = 'https://official-joke-api.appspot.com/random_joke'

    # def post(self, request):
    #     response = requests.get(self.api_url)
    #     # Посмотреть что такое response data
    #     self.serializer_class.save_response(response.json(), response_data=response.json())
    #     return Response(response.json(), status=response.status_code)
