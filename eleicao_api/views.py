from django.shortcuts import render
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from eleicao_api.models import *
from django.contrib.auth.models import User
from eleicao_api.serializers import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer
