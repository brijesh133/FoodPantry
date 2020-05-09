from inventory.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
 class Meta:
  model = User
  fields = ['username', 'email']


class InventorySerializer(serializers.HyperlinkedModelSerializer):
  donor_name = serializers.CharField(source='donor', read_only=True)
  class Meta:
   user = UserSerializer()
   model = inventory
   fields = ('name','registration_D','expiry_D','price','quantity','donor_name')