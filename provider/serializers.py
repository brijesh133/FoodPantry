from provider.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
 class Meta:
  model = User
  fields = ['username', 'email']


class ProviderSerializer(serializers.HyperlinkedModelSerializer):
  Donor_name = serializers.CharField(source='donor_name', read_only=True)
  class Meta:
   user = UserSerializer()
   model = provider
   fields = ('Donor_name','user_name','donor_status')