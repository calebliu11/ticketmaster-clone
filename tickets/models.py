from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify  

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

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.CharField(max_length=100) 
    description = models.TextField(max_length=300)
    price = models.IntegerField(default=0)
    status = models.TextField(choices=STATUS_CHOICES, default=ACTIVE)
    date = models.DateField(blank=True)
    slug = models.SlugField(null=True) 
    
    @property
    def user_email(self):
        return self.user.email

    def get_absolute_url(self):
        return f'/listings/{self.slug}/'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
             self.slug = slugify(self.event)
        return super().save(*args, **kwargs)