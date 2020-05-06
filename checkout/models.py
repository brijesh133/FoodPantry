from django.db import models
from inventory.models import inventory

# Create your models here.
class checkout(models.Model):
    item_in_inventory = models.ForeignKey(inventory, on_delete=models.SET_NULL,null=True)
    item_name = models.CharField(max_length=100, default="Wait")
    student_id = models.CharField(max_length=9)
    checkout_date = models.DateField(auto_now=True)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(default=0)
    donor = models.CharField(max_length=50, default="wait")
    def __str__(self):
          return self.student_id
