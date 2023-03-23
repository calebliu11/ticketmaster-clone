from django.urls import path

from tickets.views import RecentListingsList, post_listing, SignupView

app_name = 'tickets'

urlpatterns = [
    path('recent-listings/', RecentListingsList.as_view()),
    path('post-listing/', post_listing),
    path('signup/', SignupView.as_view()),
]
