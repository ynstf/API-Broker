from broker.serializers import SalesmanSerializer, BrokerSerializer, ReservationSerializer, BuyerSerializer, ProductSerializer
from broker.models import Salesman, Broker, Reservation, Buyer, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse

@api_view(['GET'])
def brokers(request):
    if request.method == 'GET':
        brokers = Broker.objects.all()
        serializer = BrokerSerializer(brokers , many=True)
        return Response(serializer.data)

