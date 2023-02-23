from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)

class Listing(models.Model):

    ACTIVE = "ACTIVE"
    SOLD = "SOLD"
    EXPIRED = "EXPIRED"

    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (SOLD, "Sold"),
        (EXPIRED, "Expired")
    ]

    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=100) 
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    status = models.TextField(choices=STATUS_CHOICES, default=ACTIVE)
    date = models.DateTimeField()