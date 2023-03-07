from django.contrib import admin
from .models import Profile, Listing
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("event",)}  # new

admin.site.register(Profile)
admin.site.register(Listing, ListingAdmin)
