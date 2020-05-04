from django.db import models
from django.contrib.auth.models import User
from provider.models import provider
# Create your models here.
class inventory(models.Model):
     donor = models.ForeignKey(provider, on_delete=models.CASCADE,related_name='donor')
     name = models.CharField(max_length=100)
     registration_D = models.DateField(auto_now=True)
     expiry_D = models.DateField()
     price = models.FloatField()
     quantity =  models.PositiveIntegerField()
     def __str__(self):
          return self.name

