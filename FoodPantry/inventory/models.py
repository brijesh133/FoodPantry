from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class inventory(models.Model):
     name = models.CharField(max_length=100)
     registration_D = models.DateField(auto_now=True)
     expiry_D = models.DateField()
     price = models.FloatField()
     quantity =  models.PositiveIntegerField()
     def __str__(self):
          return self.name


class profile(models.Model):
     user = models.OneToOneField(User,on_delete=models.CASCADE)

