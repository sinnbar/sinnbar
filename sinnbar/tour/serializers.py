from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Provider, Offer, Tour, Reservation, Image, Participant


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ['id', 'company', 'first_name', 'last_name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'description', 'offer', 'image', 'default']


class OfferSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'description', 'provider', 'price', 'images']


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['id', 'date', 'max_participants', 'min_participants', 'offer', 'participants']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'first_name', 'last_name', 'email']


class ReservationSerializer(WritableNestedModelSerializer):
    participant = ParticipantSerializer()

    class Meta:
        model = Reservation
        fields = ['id', 'tour', 'participant', 'number_participants', 'total_price', 'order_id']
