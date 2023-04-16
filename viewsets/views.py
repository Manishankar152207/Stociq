from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
# Create your views here.

class ViewSetApi(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer