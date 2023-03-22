from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from tickets.views import RecentListingsList, post_listing, ListingDetail

app_name = 'tickets'

urlpatterns = [
    path('recent-listings/', RecentListingsList.as_view()),
    path('post-listing/', post_listing),
    path('listings/<slug:listing_slug>', ListingDetail.as_view()),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)