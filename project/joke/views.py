from random import randint
import requests
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Joke
from .serializers import JokeSerializer
from django.conf import settings


class BaseDocumentPostView(APIView):
    permission_classes = [AllowAny]
    serializer_class = None
    api_url = None

    def post(self, request):
        response = requests.get(self.api_url)
        self.serializer_class.save_response(response.json(), response_data=response.json())
        return Response(response.json(), status=response.status_code)


class JokeView(BaseDocumentPostView, APIView):
    serializer_class = JokeSerializer
    api_url = settings.URL_JOKES

    def get(self, request):
        id_count = Joke.objects.count()
        return Response(Joke.objects.filter(id=randint(1, id_count)).values("joke_setup",
                                                                            "joke_punchline",
                                                                            )
                        )
