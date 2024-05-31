from api.serializers import CitySerializer
from api.models import City
from rest_framework import viewsets

class CityViewsets(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer