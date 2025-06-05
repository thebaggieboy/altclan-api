from rest_framework import serializers

from .models import *
class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'sender', 'notification_type', 
                  'message', 'is_read', 'created_at', 'target_url']   

