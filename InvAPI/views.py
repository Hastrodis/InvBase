from django.shortcuts import render
from django.contrib.auth.models import User
from SaveBase.models import Techn, History, Type
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, TechSerializer, HistSerializer, TypeSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet): # только для чтения
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class TechViewSet(viewsets.ModelViewSet):
    queryset = Techn.objects.all()
    serializer_class = TechSerializer
    permission_classes = [permissions.IsAuthenticated]

class HistViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistSerializer
    permission_classes = [permissions.IsAuthenticated]

class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [permissions.IsAuthenticated]
