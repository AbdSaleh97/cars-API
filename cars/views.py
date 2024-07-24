from django.shortcuts import render

from .models import Car
# from .serializers import CarSerilaizer
from rest_framework import generics
from .serializers import CarSerilaizer

# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerilaizer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerilaizer
    


