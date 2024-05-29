from api.serializers import SalesmanSerializer, BrokerSerializer, ReservationSerializer, BuyerSerializer, ProductSerializer, CitySerializer
from api.models import Salesman, Broker, Reservation, Buyer, Product, City
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, mixins, viewsets


class CityViewsets(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer