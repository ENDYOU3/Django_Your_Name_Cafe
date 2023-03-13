from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return '{} : {}'.format(self.title, self.email)


class Customer(models.Model):
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
    country = models.CharField(max_length = 60)
    city = models.CharField(max_length = 60)
    address = models.CharField(max_length = 225)
    phone = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    def __str__(self) -> str:
    	return f'{self.first_name} {self.last_name}'


class Shipping(models.Model):
    STATUS = [
        ('Disapproved', 'Disapproved'), 
        ('Approve', 'Approve'), 
        ('Banned', 'Banned')
    ]
    PAYMENT = [
        ('Cash On Delivery', 'Cash On Delivery'),
        ('Bank Transfer', 'Bank Transfer')
    ]
    payment_method = models.CharField(max_length = 50, choices = PAYMENT, default = 'Cash On Delivery')
    note = models.CharField(max_length = 100, null = True)
    status = models.CharField(max_length = 50, choices = STATUS, default = 'Disapproved')
    shipping_date = models.DateTimeField(auto_now_add = True)
    customer = models.ForeignKey('app_general.Customer', on_delete = models.CASCADE, null = True)


class Order(models.Model):
    product = models.ForeignKey('app_product.Product',  on_delete = models.CASCADE, null = True)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    shipping = models.ForeignKey('app_general.Shipping', on_delete = models.CASCADE, null = True)