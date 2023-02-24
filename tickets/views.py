from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Listing
from .serializers import ListingSerializer

# Create your views here.

class RecentListingsList(APIView):
    def get(self, request, format=None):
        listings = Listing.objects.all()[0:5]
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
