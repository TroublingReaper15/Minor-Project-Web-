from django.db import models
from datetime import datetime,date
# Create your models here.
class Subscribe(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)

class User(models.Model):
    name= models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    password= models.CharField(max_length=100)

class Coupon(models.Model):
    code= models.CharField(max_length=100)

class Billing(models.Model):
    country= models.CharField(max_length=100)
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    company= models.CharField(max_length=100, null=True, blank=True)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    zip_code= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    phone_number= models.CharField(max_length=100)
    order_notes= models.TextField(null=True, blank=True)
    coupon= models.ForeignKey(Coupon, on_delete=models.CASCADE)