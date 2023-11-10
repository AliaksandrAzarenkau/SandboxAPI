from rest_framework import serializers

from .models import Joke


class JokeResponseHandling:
    def save_response(self, response_data):
        j_id = response_data.get('id')
        category = response_data.get('type')
        setup = response_data.get('setup')
        punchline = response_data.get('punchline')

        request_data = Joke(
            joke_id=j_id,
            joke_category=category,
            joke_setup=setup,
            joke_punchline=punchline
        )
        request_data.save()


class JokeSerializer(serializers.ModelSerializer, JokeResponseHandling):
    class Meta:
        model = Joke
        fields = '__all__'
