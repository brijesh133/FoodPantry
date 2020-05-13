from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class provider(models.Model):
    donor_name = models.CharField(max_length=50,primary_key=True )
    user_name = models.CharField(max_length=50, default="User")
    donor_status = models.CharField(max_length=50)
    anonymus_status = models.BooleanField(default=False)
    def __str__(self):
          return self.donor_name
