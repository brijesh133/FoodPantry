from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class provider(models.Model):
    donor_name = models.CharField(max_length=50,primary_key=True )
    donor_status = models.CharField(max_length=50)
    anonymous_status = models.CharField(max_length=3)
    def __str__(self):
          return self.donor_name
