from django.contrib import admin

from .models import Listing, Report, Order, Account, Event
# Register your models here.

admin.site.register(Event)
admin.site.register(Listing)
admin.site.register(Report)
admin.site.register(Order)
admin.site.register(Account)