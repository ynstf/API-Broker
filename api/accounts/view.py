from api.serializers import SalesmanSerializer, BrokerSerializer, ReservationSerializer, BuyerSerializer, ProductSerializer
from api.models import Salesman, Broker, Reservation, Buyer, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class Brokers(APIView):
    def get(self, request):
        brokers = Broker.objects.all()
        serializer = BrokerSerializer(brokers, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BrokerSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
    

class BrokerID(APIView):
    def get_broker(self, pk):
        try:
            return Broker.objects.get(id=pk)
        except Broker.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        broker = self.get_broker(pk)
        serializer = BrokerSerializer(broker)
        return Response(serializer.data)
    
    def put(self, request, pk):
        broker = self.get_broker(pk)
        serializer = BrokerSerializer(broker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        broker = self.get_broker(pk)
        broker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class Salers(APIView):
    def get(self, request):
        salers = Salesman.objects.all()
        serializer = SalesmanSerializer(salers, many = True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SalesmanSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status= status.HTTP_400_BAD_REQUEST
        )
    

class SalerID(APIView):
    def get_saler(self, pk):
        try:
            return Salesman.objects.get(id=pk)
        except Salesman.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        saler = self.get_saler(pk)
        serializer = SalesmanSerializer(saler)
        return Response(serializer.data)
    
    def put(self, request, pk):
        saler = self.get_saler(pk)
        serializer = SalesmanSerializer(saler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        saler = self.get_saler(pk)
        saler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

