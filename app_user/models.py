from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=225)
    phone = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return f'{self.user} | {self.country} {self.city}'