from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify  

# Create your models here.

class Listing(models.Model):

    ACTIVE = "ACTIVE"
    SOLD = "SOLD"
    EXPIRED = "EXPIRED"

    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (SOLD, "Sold"),
        (EXPIRED, "Expired")
    ]

    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_email = models.CharField(max_length=100)
    event = models.CharField(max_length=100, unique=False) 
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    status = models.TextField(choices=STATUS_CHOICES, default=ACTIVE)
    date = models.DateField(blank=True)
    slug = models.SlugField(null=True) 
    image = models.ImageField(upload_to='pics', null=True, blank=True)
 
    def get_absolute_url(self):
        return f'/listings/{self.slug}/'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
             self.slug = slugify(self.event)
        return super().save(*args, **kwargs)
    
class Order(models.Model):
    user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    cost = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id',]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    event = models.CharField(max_length=100, unique=False) 
    description = models.TextField(max_length=300)
    listing = models.ForeignKey(Listing, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    seller_email = models.CharField(max_length=100)
    date = models.DateField(blank=True)
    image_url = models.CharField(max_length=100)
