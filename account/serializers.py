from rest_framework import serializers
from django.conf import settings
from .models import Profile, CustomUser, BrandUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']

class BrandUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandUser
        fields = ['email', 'password']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['id',  'first_name', 'last_name', 'email_address', 'mobile_number', 'display_picture', 'billing_address', 'city', 'state', 'zip']


