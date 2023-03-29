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
    event = models.CharField(max_length=100, unique=False) 
    user_email = models.CharField(max_length=100)
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