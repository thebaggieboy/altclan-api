from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Merchandise, Cart, Leads, BrandDashboard
from django.conf import settings
from accounts.models import BrandProfile


BrandUser = settings.BRAND_USER_MODEL



class BrandProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandProfile
        fields = ['id','user','date_created']

class BrandDashboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandDashboard
        fields = ['total_views', 'total_products', 'total_users', 'total_profit']



class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['id','brand_name', 'instagram_username', 'website_link']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'id','brand_name', 'merchandise_name', 'merchandise_size', 'labels', 'delivery_cost', 'category', 'merchandise_description', 'merchandise_details', 'price', 'display_image',
        ]
        

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','quantity', 'merchandises']
