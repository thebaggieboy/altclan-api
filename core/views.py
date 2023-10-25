from django.shortcuts import render
from rest_framework import viewsets
from account.models import * 
from account.serializers import *
from brands.models import *
from brands.serializers import *
from reviews.models import *
from reviews.serializers import *
from transactions.serializers import *
from transactions.models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Create your views here.

# Create your views here.
class BrandProfileViewSet(viewsets.ModelViewSet):
    queryset = BrandProfile.objects.all()
    serializer_class = BrandProfileSerializer
    


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    


class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    


class RefundViewSet(viewsets.ModelViewSet):
    queryset = Refund.objects.all()
    serializer_class = RefundSerializer
    



    


