from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tickets.views import RecentListingsList, post_listing, ListingDetail, AddListingToEvent, LoginView, ListingsList, checkout, OrdersList

app_name = 'tickets'

urlpatterns = [
    path('recent-listings/', RecentListingsList.as_view()),
    path('post-listing/', post_listing),
    path('listings/<slug:listing_slug>', ListingDetail.as_view()),
    path('listings/sell/<slug:listing_slug>', AddListingToEvent.as_view()),
    path('login/', LoginView.as_view()),
    path('listings/', ListingsList.as_view()),
    path('checkout/', checkout),
    path('orders/', OrdersList.as_view())
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
