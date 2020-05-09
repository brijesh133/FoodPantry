from checkout.models import *
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
 class Meta:
  model = User
  fields = ['username', 'email']


class CheckoutSerializer(serializers.HyperlinkedModelSerializer):
  item = serializers.CharField(source='item_in_inventory', read_only=True)
  class Meta:
   user = UserSerializer()
   model = checkout
   fields = ('item','student_id','checkout_date','price','quantity')