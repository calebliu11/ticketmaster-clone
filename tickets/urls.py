from django.urls import path

from tickets.views import RecentListingsList

app_name = 'tickets'

urlpatterns = [
    path('recent-listings/', RecentListingsList.as_view())
]
