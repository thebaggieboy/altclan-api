from rest_framework import serializers
from django.conf import settings
from .models import Profile, CustomUser, BrandUser
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer


# Custom Serializer for Djoser Library 
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id',  'email',  'password' ]
        
        



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'user_type', 'email', 'first_name', 'last_name', 'mobile_number', 'billing_address', 'state', 'city', 'zip', 'display_picture', 'following', 'wish_list']

class BrandUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandUser
        fields = ['id', 'email', 'brand_name', 'brand_logo',  'brand_bio', 'brand_type', 'mobile_number']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='profile-detail',queryset=Profile.objects.all())
    class Meta:
        model = Profile
        fields = ['id', 'user', 'date_created']


