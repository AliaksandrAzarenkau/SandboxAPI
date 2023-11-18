from rest_framework import serializers
from .models import Entertainments


class EntertainmentsResponseHandling:
    def save_response(self, response_data):
        activity = response_data.get('activity')
        type = response_data.get('type')
        participants = response_data.get('participants')
        price = response_data.get('price')
        link = response_data.get('link')
        key = response_data.get('key')
        accessibility = response_data.get('accessibility')

        if not Entertainments.objects.filter(entertainment=activity).exists():
            Entertainments.objects.create(
                category=type,
                entertainment=activity,
                participants=participants,
                price=price,
                accessibility=accessibility,
                entertainment_id=key,
                link=link,
            )


class EntertainmentsSerializer(serializers.ModelSerializer, EntertainmentsResponseHandling):
    class Meta:
        model = Entertainments
        fields = '__all__'


class EntertainmentsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entertainments
        fields = ("entertainment",
                  "participants",
                  "price",
                  "accessibility",
                  )
