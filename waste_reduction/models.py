from django.db import models

# Create your models here.
class wastage(models.Model):
    item_name = models.CharField(max_length=100)
    registration_D = models.DateField()
    expiry_D = models.DateField()
    price = models.FloatField()
    quantity =  models.PositiveIntegerField()
    donor = models.CharField(max_length=100)