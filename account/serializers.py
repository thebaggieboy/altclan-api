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
        fields = ['id', 'email', 'password']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='profile-detail',queryset=Profile.objects.all())
    class Meta:
        model = Profile
        fields = ['id', 'user', 'first_name', 'last_name', 'email_address', 'mobile_number', 'display_picture', 'billing_address', 'city', 'state', 'zip']


