from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Listing
from .serializers import ListingSerializer

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class SellerView(TemplateView):
    template_name = "seller.html"

class BuyerView(TemplateView):
    template_name = "buyer.html"

class RecentListingsList(APIView):
    def get(self, request, format=None):
        listings = Listing.objects.all()[0:5]
        serializer = ListingSerializer
        return Response(serializer.data)
