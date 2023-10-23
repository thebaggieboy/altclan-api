from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Merchandise, Cart, Leads
from django.conf import settings

BrandUser = settings.BRAND_USER_MODEL

from account.models import BrandProfile



class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'user', 'brand_name', 'brand_logo', 'brand_bio', 'slug', 'followers']

class BrandProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandProfile
        fields = ['id','user','brand_name', 'brand_bio', 'brand_logo',  'mobile_number',  'followers',  'billing_address', 'city', 'state', 'zip']


class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['id','brand_name', 'instagram_username', 'website_link']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'id','brand', 'merchandise_name', 'merchandise_size', 'labels', 'delivery_cost', 'category', 'price', 'display_image',
        ]
        

class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','quantity', 'merchandises']
