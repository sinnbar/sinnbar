from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import UserViewSet, ProviderViewSet, OfferViewSet, ImageViewSet, TourViewSet, ParticipantViewSet, \
    ReservationViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'providers', ProviderViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'images', ImageViewSet)
router.register(r'tours', TourViewSet)
router.register(r'participants', ParticipantViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh_token/", TokenRefreshView.as_view(), name="refresh_token"),

]
