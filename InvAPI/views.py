from django.shortcuts import render
from django.contrib.auth.models import User
from SaveBase.models import Techn, History, Type
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, TechSerializer, HistSerializer, TypeSerializer, SearchSerializer
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from InvBase.document import TechDocument
from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_RANGE,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)

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

class SearchViewSet(DocumentViewSet):
    document = TechDocument
    serializer_class = SearchSerializer

    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
    ]

    # Define search fields
    search_fields = (
        'InvNomer',
        'Naimen',
    )

    filter_fields = {
        'InvNomer': 'InvNomer.raw',
        'Naimen': 'Naimen.raw',
    }

