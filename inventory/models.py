from django.db import models

# Create your models here.

class Inventory(models.Model):
    name=models.CharField(max_length=30)
    quantity=models.IntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)