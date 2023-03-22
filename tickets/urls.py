from django.urls import path

from tickets.views import RecentListingsList, post_listing, signup

app_name = 'tickets'

urlpatterns = [
    path('recent-listings/', RecentListingsList.as_view()),
    path('post-listing/', post_listing),
    path('signup/', signup),
]
