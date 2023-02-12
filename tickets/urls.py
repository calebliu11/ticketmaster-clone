from django.urls import path

from tickets.views import HomeView, SellerView, BuyerView

app_name = 'tickets'

urlpatterns = [
    path('', HomeView.as_view(), name='homepage'),
    path('seller/', SellerView.as_view(), name='seller'),
    path('buyer/', BuyerView.as_view(), name='buyer'),
]
