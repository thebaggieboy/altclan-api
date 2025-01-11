from rest_framework import serializers
from django.contrib.auth.models import User
from .models import  Merchandise, Leads
from django.conf import settings
 
from brands.models import WishList


class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['id','brand_name', 'instagram_username', 'website_link']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'id','brand_name', 'merchandise_name', 'available_sizes', 'available_colors', 'labels', 'delivery_cost',  'merchandise_description', 'merchandise_details', 'price', 'display_image',
        ]
        


class WishListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WishList
        fields = [
            'id', 'product_name', 'display_image', 'colors',  'quantity' 
        ]
        
