from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

class SellerView(TemplateView):
    template_name = "seller.html"

class BuyerView(TemplateView):
    template_name = "buyer.html"
