from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tickets.views import RecentEventsList, create_event, post_listing, ListingDetail, AddListingToEvent, LoginView, ListingsList, checkout, OrdersList, update_listings, report, search, AccountView, cashout, check_transfer, signup, activate, get_event

app_name = 'tickets'

urlpatterns = [
    path('recent-events/', RecentEventsList.as_view()),
    path('create-event/', create_event),
    path('post-listing/', post_listing),
    path('listings/<slug:listing_slug>', ListingDetail.as_view()),
    path('listings/sell/<slug:listing_slug>', AddListingToEvent.as_view()),
    path('login/', LoginView.as_view()),
    path('listings/', ListingsList.as_view()),
    path('checkout/', checkout),
    path('orders/', OrdersList.as_view()),
    path('update-listings/', update_listings),
    path('report/', report),
    path('search/', search),
    path('account/', AccountView.as_view()),
    path('cashout/', cashout),
    path('check-transfer/', check_transfer),
    path('signup/', signup),
    path('activate/<uidb64>/<token>', activate),
    path('get-event/<slug:listing_slug>', get_event)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
