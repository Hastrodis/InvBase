from django.contrib.auth.models import User
from SaveBase.models import Techn, History, Type
from rest_framework import serializers
from InvBase.document import TechDocument
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name']

class TechSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Techn
        fields = ['url', 'IDUser', 'IDType', 'InvNomer', 'Naimen', 'DataProverki', 'Prim']
        read_only_fields = ['IDType']

class HistSerializer(serializers.HyperlinkedModelSerializer):
    #histnom = serializers.SerializerMethodField('getidentifier')
    class Meta:
        model = History
        fields = ['url', 'FIOPod', 'DataPerem']

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ['TypeTech']

class SearchSerializer(DocumentSerializer):
    class Meta:
        document = TechDocument
        fields = ['InvNomer', 'Naimen']
