from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Listing
from .serializers import ListingSerializer
from django.core.exceptions import ValidationError

from datetime import date
from datetime import datetime
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User

# Create your views here.

@api_view(['POST'])
def post_listing(request):
    serializer = ListingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        serializer.save(user=request.user, event=data['event'], user_email=data['user_email'], description=data['description'], price=data['price'], date=data['date'], image=data['image'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except ValidationError:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
        
class AddListingToEvent(APIView):
    def get_object(self, listing_slug):
        try:
            return Listing.objects.filter(slug=listing_slug)[0]
        except Listing.DoesNotExist:
            raise Http404

    def get(self, request, listing_slug, format=None):  
        listing = self.get_object(listing_slug)
        serializer = ListingSerializer(listing)
        if isinstance(serializer.data, list):
            return Response(serializer.data)
        else:
            return Response([serializer.data])
        
class UserDetail(APIView):
    def get(self, request, username, format=None):
        user = User.objects.get(username = username)
        if (user.id == '' or user.id == None):
            return Response({
                'status': False,
                'id': 'Has not set id'
            })
        else:
            return Response({
                'status': True,
                'id': user.id
            })