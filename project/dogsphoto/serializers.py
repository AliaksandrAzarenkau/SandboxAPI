from rest_framework import serializers

from .models import DogsPhoto


class DogsPhotoResponseHandling:
    def save_response(self, response_data):
        link = response_data.get('message')
        status = response_data.get('status')

        if not DogsPhoto.objects.filter(message=link).exists():
            DogsPhoto.objects.create(
                message=link,
                status=status,
            )


class DogsPhotoSerializer(serializers.ModelSerializer, DogsPhotoResponseHandling):
    class Meta:
        model = DogsPhoto
        fields = ('message',
                  'status',
                  'start_data',
                  )
