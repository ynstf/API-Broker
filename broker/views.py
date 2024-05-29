from .serializers import SalesmanSerializer, BrokerSerializer, ReservationSerializer, BuyerSerializer, ProductSerializer
from .models import Salesman, Broker, Reservation, Buyer, Product
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import JsonResponse

@api_view(['GET','POST'])
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            error = {"message" : "error to save this product"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def find_product(request):
    name = request.data['name']
    products = Product.objects.filter(name__icontains=name)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def product(request, pk):

    #check if this product exist
    try :
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        error = {"message" : "this product does not exist"}
        return Response(error, status=status.HTTP_404_NOT_FOUND)

    #get infos if GET
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    #update infos if PUT
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            error = {"message" : "error to update this product"}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    #delete the product if DELETE
    if request.method == 'DELETE':
        product.delete()
        message = {"message" : "this product deleted ", 'data':ProductSerializer(product).data}
        return Response(message, status=status.HTTP_200_OK)
