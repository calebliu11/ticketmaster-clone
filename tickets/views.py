import stripe

from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions

from .models import Listing, Order
from .serializers import ListingSerializer, OrderSerializer
from django.core.exceptions import ValidationError

from datetime import date
from datetime import datetime
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token

# Create your views here.

@api_view(['POST'])
def post_listing(request):
    serializer = ListingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        email=request.user.email
        serializer.save(user=request.user, user_email=email, event=data['event'], description=data['description'], price=data['price'], date=data['date'], image=data['image'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except ValidationError:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)

            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

        else:
            return Response({'error': 'Invalid username or password, user not found'}, status=status.HTTP_404_NOT_FOUND)

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

class ListingsList(APIView):
    def get(self, request, format=None):
        listings = Listing.objects.filter(user=request.user)
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
    
@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        total_cost = sum(item.get('listing').price for item in serializer.validated_data['items'])

        print(serializer.validated_data['stripe_token'])
        try: 
            charge = stripe.Charge.create(
                amount = int(total_cost * 100),
                currency = 'USD',
                description = 'Purchase from TicketTrade',
                source = serializer.validated_data['stripe_token']
            )

            serializer.save(user=request.user, cost=total_cost)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)