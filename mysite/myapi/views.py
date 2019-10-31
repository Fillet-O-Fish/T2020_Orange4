from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
# Create your views here.

from rest_framework import viewsets

from .apiCalls import UserSerializer
from .models import user
from .main import init

class UserViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all().order_by('name')
    serializer_class = UserSerializer

class userDetail(generic.TemplateView):
    def get(self,request):
        userInfo = main.init("limzeyang")
        return userInfo