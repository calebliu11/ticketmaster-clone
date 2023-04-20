import stripe

from django.shortcuts import render
from django.conf import settings


from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib import messages
from django.http import HttpResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status, authentication, permissions

from .models import Listing, Order, Account, Report, Event
from .serializers import ListingSerializer, OrderSerializer, ReportSerializer, AccountSerializer, EventSerializer
from django.core.exceptions import ValidationError

from datetime import date
from datetime import datetime
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.authtoken.models import Token
import json
from django.http import JsonResponse
from django.db.models import Q, F
from bson.decimal128 import Decimal128
from decimal import Decimal
from .forms import UserRegistrationForm

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from rest_framework.renderers import JSONRenderer

# Create your views here.

@api_view(['POST'])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    try:
        reports = Report.objects.filter(reported_user=request.user)
        if reports.count() >= 3:
            return Response('User has been reported too many times and is banned from posting listings or creating events.', status=status.HTTP_403_FORBIDDEN)

        existing_event = Event.objects.filter(name__iexact=request.data['name']).first()
        if existing_event is not None:
            return JsonResponse({'errors': 'Event already exists with this name!'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        serializer.save(name=data['name'], description=data['description'], date=data['date'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    except ValidationError:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_listing(request):
    serializer = ListingSerializer(data=request.data)

    try:
        reports = Report.objects.filter(reported_user=request.user)
        if reports.count() >= 3:
            return Response('User has been reported too many times and is banned from posting listings or creating events.', status=status.HTTP_403_FORBIDDEN)

        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        username = request.user.username
        serializer.save(user=request.user, user_username=username, event=data['event'], price=data['price'], image=data['image'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except ValidationError:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = User.objects.filter(username=username).first()

        if user is not None:
            if user.is_active:
                authenticated_user = authenticate(username=username, password=password)
                if authenticated_user is not None:
                    login(request, authenticated_user)

                    token, created = Token.objects.get_or_create(user=authenticated_user)
                    return Response({'token': token.key})
                else: 
                    return JsonResponse({'errors': 'Invalid username or password.'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse({'errors': 'Account not verified, please check your email'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'errors': 'Invalid username or password, user not found'}, status=status.HTTP_404_NOT_FOUND)

class RecentEventsList(APIView):
     def get(self, request, format=None):
        current_date = datetime.now().date()
        events = Event.objects.order_by('date').filter(date__gte=current_date)[0:25]
      
        unique_events = []
        list = []
        for x in events: 
            if x.slug not in list: 
                unique_events.append(x)
                list.append(x.slug)
        serializer = EventSerializer(unique_events, many=True)
        return Response(serializer.data)

class ListingDetail(APIView):
    def get_object(self, listing_slug):
        try:
            return Listing.objects.all().filter(slug=listing_slug, status="ACTIVE")
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, listing_slug, format=None):  
        listings = self.get_object(listing_slug).exclude(user=request.user)
        serializer = ListingSerializer(listings, many=True)
        if isinstance(serializer.data, list):
            return Response(serializer.data)
        else:
            return Response([serializer.data])

@api_view(['GET'])
def get_event(request, listing_slug):
    event = Event.objects.filter(slug=listing_slug).first()
    serializer = EventSerializer(event, many=False)
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
                    description = "Order from " + str(request.user),
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
        current_date = datetime.now().date()
        events = Event.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query), date__gte=current_date)
        serializer = EventSerializer(events, many=True)
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

        if user_account is None:
            user_account = Account.objects.create(user=request.user)

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
    
    if user_account is None:
        return Response("Account not created yet.", status=status.HTTP_200_OK)

    stripe_account = stripe.Account.retrieve(user_account.account_id)
    capabilities = stripe_account['capabilities']
    return Response(capabilities, status=status.HTTP_200_OK)

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        #When you click on link it takes you page
        # messages.success(request,"Success: Account verified. You can close this page!")

      
        return render(request, 'success.html')
        # return HttpResponse("Success: Account verified. You can close this page!")
    else:
        return HttpResponse("Error: Account not able to be verified. Please try again.")


def activate_email(request, user, email):
    mail_subject = 'Activate your user account with TicketSwap.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[email])
    if email.send():
        return HttpResponse("f'{user}, please go to your email <b>{email}</b> inbox and click on the activation link to verify your \
                account. Make sure to check your spam folder.")
    else:
        return HttpResponse("Error with sending verification email")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        existing_user = User.objects.filter(username=username).first()
        if existing_user is not None:
            return JsonResponse({'errors': 'User already exists with this username!'}, status=status.HTTP_400_BAD_REQUEST)

        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()

            activate_email(request, user, form.cleaned_data.get('email'))
            return HttpResponse("Email successfully sent!")
        else:
            errors_dict = {}
            for field, field_errors in form.errors.items():
                errors_dict[field] = [str(e) for e in field_errors]
            return JsonResponse({'errors': errors_dict}, status=status.HTTP_400_BAD_REQUEST)
    else:
        form = UserRegistrationForm()

@api_view(['POST'])
def delete_listing(request, listing_slug):
    listing = Listing.objects.filter(slug=listing_slug).first()
    if listing is not None:
        listing.delete()
        return JsonResponse({'success': 'Listing deleted.'}, status=status.HTTP_200_OK)
    return JsonResponse({'errors': 'Listing does not exist.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def edit_listing(request, listing_slug):
    listing = Listing.objects.filter(slug=listing_slug).first()
    if listing is not None:
        listing.price = request.data.get('price')
        listing.save()
        return JsonResponse({'success': 'Listing updated.'}, status=status.HTTP_200_OK)
    return JsonResponse({'errors': 'Listing does not exist.'}, status=status.HTTP_404_NOT_FOUND)


    