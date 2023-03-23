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

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

@api_view(['POST'])
def post_listing(request):
    serializer = ListingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        updated_datetime = datetime.combine(data['date'], datetime.min.time())
        serializer.save(id=data['id'], event=data['event'], description=data['description'], price=data['price'], date=updated_datetime)
    except ValidationError:
        print(serializer.errors)

    return Response(serializer.initial_data)

class RecentListingsList(APIView):
    def get(self, request, format=None):
        listings = Listing.objects.all()[0:12]
        serializer = ListingSerializer(listings, many=True)
        return Response(serializer.data)

class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        User = get_user_model()
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        
        subject = 'Verify your email address with TicketTrade.'
        verification_url = f'/api/v1/verify/?uid={uid}&token={token}'
        message = f'Please click the following link to verify your email address: {verification_url}'
        send_mail(subject, message, , [email], fail_silently=False)

        return Response({'detail': 'Verification email sent successfully.'}, status=status.HTTP_201_CREATED)