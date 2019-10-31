from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .apiCalls import UserSerializer
from .models import Hero


class UserViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = UserSerializer