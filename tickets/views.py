from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Listing
from .serializers import ListingSerializer
from django.core.exceptions import ValidationError

from datetime import date
from datetime import datetime
from django.http import Http404, HttpResponse

# Create your views here.

@api_view(['POST'])
def post_listing(request):
    serializer = ListingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        serializer.save(event=data['event'], description=data['description'], price=data['price'], date=data['date'], image=data['image'])
    except ValidationError:
        print(serializer.errors)

    return Response(serializer.initial_data)

class RecentListingsList(APIView):
     def get(self, request, format=None):
        listings = Listing.objects.order_by('date','price').distinct()[0:25]
        unique_listings = []
        list = []
        for x in listings: 
            if x.slug not in list: 
                unique_listings.append(x)
                list.append(x.slug)
        serializer = ListingSerializer(unique_listings, many=True)
        return Response(serializer.data)

class ListingDetail(APIView):
    def get_object(self, listing_slug):
        try:
            return Listing.objects.all().filter(slug=listing_slug)
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, listing_slug, format=None):  
        listings = self.get_object(listing_slug)
        serializer = ListingSerializer(listings, many=True)
        if isinstance(serializer.data, list):
            return Response(serializer.data)
        else:
            return Response([serializer.data])