from rest_framework import serializers

from .models import *
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id','order_date', 'ordered', 'delivered', 'tracking_number', 'number_of_items']



class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['paystack_charge_id', 'amount', 'status', 'timestamp']


class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'amount']



class RefundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refund
        fields = ['id', 'order', 'reason', 'accepted', 'email' ]



