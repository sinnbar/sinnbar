from django.contrib.auth.models import User
from django.template.loader import render_to_string
from rest_framework import viewsets, status

# ViewSets define the view behavior.
from rest_framework.decorators import action
from rest_framework.response import Response

from sinnbar.settings import HOST
from .helpers import send_email_to_participant
from .models import Provider, Offer, Image, Tour, Participant, Reservation
from .serializers import UserSerializer, ProviderSerializer, OfferSerializer, ImageSerializer, TourSerializer, \
    ParticipantSerializer, ReservationSerializer
from .utils import GetOrder


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer
    authentication_classes = []


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filterset_fields = ['offer']
    authentication_classes = []


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    authentication_classes = []

    def create(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        print(request.data)
        headers = self.get_success_headers(request.data)
        order_data = request.data.pop('orderData')
        order_id = order_data['orderID']
        # ________________
        get_order_instance = GetOrder()
        order_response = get_order_instance.get_order(order_id)
        if order_response.result.status == 'COMPLETED':
            print(request.data['bookingData'])
            request.data['order_id'] = order_id
            request.data['total_price'] = order_response.result.purchase_units[0].amount.value
            serializer = self.get_serializer(data=request.data['bookingData'])
            serializer.is_valid(raise_exception=True)

            reservation = serializer.save()
            context = reservation.__dict__
            context['HOST'] = HOST
            text_content = render_to_string('email/participant/confirmation_email.txt', reservation.__dict__)
            html_content = render_to_string('email/participant/confirmation_email.html', reservation.__dict__)
            send_email_to_participant('sinnbar | Bestätigung ihrer Buchung!', text_content, html_content,
                                      reservation.participant.email)

            return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)
            #return Response(status=status.HTTP_402_PAYMENT_REQUIRED, headers=headers)
        else:
            return Response(status=status.HTTP_402_PAYMENT_REQUIRED, headers=headers)



