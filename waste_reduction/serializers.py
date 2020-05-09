from waste_reduction.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
 class Meta:
  model = User
  fields = ['username', 'email']


class WasteSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
   user = UserSerializer()
   model = wastage
   fields = ('item_name','registration_D','expiry_D','price','quantity','donor')