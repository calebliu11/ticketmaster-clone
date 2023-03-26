from django.contrib import admin
from .models import Listing
# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("event",)}  

admin.site.register(Listing, ListingAdmin)