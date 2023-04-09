import stripe

from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions

from .models import Listing, Order, Account, Report
from .serializers import ListingSerializer, OrderSerializer, ReportSerializer, AccountSerializer
from django.core.exceptions import ValidationError

from datetime import date
from datetime import datetime
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
import json
from django.http import JsonResponse
from django.db.models import Q, F
from bson.decimal128 import Decimal128
from decimal import Decimal

# Create your views here.

@api_view(['POST'])
def post_listing(request):
    serializer = ListingSerializer(data=request.data)
    try:
        reports = Report.objects.filter(reported_user=request.user)
        if reports.count() >= 3:
            return Response('User has been reported too many times and is banned from posting listings.', status=status.HTTP_403_FORBIDDEN)

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
        listings = Listing.objects.order_by('date','price').distinct().filter(status="ACTIVE")[0:25]
      
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
            return Listing.objects.all().filter(slug=listing_slug, status="ACTIVE")
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

        for item in serializer.validated_data['items']:
            user_account = Account.objects.filter(user=item['user']).first()
            if user_account is None:
                user_account = Account.objects.create(user=item['user'])
            
            user_account.funds = Decimal(str(user_account.funds)) + Decimal(item["price"])
            user_account.save()

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
    
@api_view(['POST'])
def update_listings(request):
    if request.method == 'POST':
        listing_ids = json.loads(request.body)
        listings = Listing.objects.none()
        for item in listing_ids:
            cur_listing = Listing.objects.filter(id=item['listing'])
            listings = listings | cur_listing

        serializer = ListingSerializer(listings, many=True)
        for i in range(len(listing_ids)):
            serializer.data[i]['status'] = "SOLD"
            listings[i].status = serializer.data[i]['status']
            listings[i].save()

        return Response(serializer.data)

@api_view(['POST'])
def report(request):
    serializer = ReportSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        serializer.save(user=request.user, reported_user=data['reported_user'], reason=data['reason'], description=data['description'], verified=data['verified'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except ValidationError:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def search(request):
    search_query = request.data.get('query', '')

    if search_query:
        listings = Listing.objects.filter(Q(event__icontains=search_query) | Q(description__icontains=search_query), status="ACTIVE")
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)
    else:
        return Response({"Empty Listings": []})
    
class AccountView(APIView):
    def get(self, request, format=None):
        account = Account.objects.filter(user=request.user)
        serializer = AccountSerializer(account.first(), many=False)
        return Response(serializer.data)
    
    def post(self, request):
        stripe.api_key = settings.STRIPE_SECRET_KEY

        user_account = Account.objects.filter(user=request.user).first()

        account = stripe.Account.create(
            country="US",
            type="express",
            capabilities={"card_payments": {"requested": True}, "transfers": {"requested": True}},
        )

        bank_account_object = {
            "object": "bank_account",
            "country": "US",
            "currency": "usd",
            "account_holder_name": "Test User",
            "account_holder_type": "individual",
            "routing_number": '110000000',
            "account_number": '000123456789',
        }

        stripe.Account.create_external_account(
            account.id,
            external_account=bank_account_object,
        )

        link = stripe.AccountLink.create(
            account=account.id,
            refresh_url="http://localhost:3000/account",
            return_url="http://localhost:3000/account",
            type="account_onboarding",
        )

        user_account.account_id = account.id
        user_account.funds = Decimal(str(user_account.funds))

        user_account.save()
        return Response(link, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def cashout(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY

    cashout_amount = int(Decimal(request.data['funds']) * 100)

    user_account = Account.objects.filter(user=request.user).first()

    payout = stripe.Transfer.create(
        amount=cashout_amount,
        currency='usd',
        destination=user_account.account_id,
    )

    user_account.funds = 0.0
    user_account.save()

    return Response(payout, status=status.HTTP_200_OK)

@api_view(['GET'])
def check_transfer(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    user_account = Account.objects.filter(user=request.user).first()
    
    stripe_account = stripe.Account.retrieve(user_account.account_id)
    capabilities = stripe_account['capabilities']

    return Response(capabilities, status=status.HTTP_200_OK)
