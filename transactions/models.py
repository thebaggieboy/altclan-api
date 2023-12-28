from django.db import models
from django.conf import settings
from accounts.models import User
import uuid
from django.utils import timezone
import uuid
from django.utils.crypto import get_random_string
from brands.models import BillingAddress
from django.utils.text import slugify

STATUS = (
    ('P', 'Pending'),
    ('C', 'Completed'),
)

from django.conf import settings

User = settings.AUTH_USER_MODEL
RANDOM_ORDER_ID = get_random_string(length=8)

STATUS = (
    ('P', 'Pending'),
    ('C', 'Completed'),
)

# Create your models here.
class Order(models.Model): 
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4().hex, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=250, default=get_random_string(length=12))
    number_of_items = models.IntegerField(null=True)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now())
    

    def __str__(self):
        return f'{self.tracking_number}'


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name='user_order')
    order = models.OneToOneField('Order', models.CASCADE, null=True, blank=True, related_name='user_payment')
    paystack_charge_id = models.CharField(max_length=50, default='', null=True, blank=True)
    amount = models.FloatField()
    status = models.CharField(max_length=250, choices=STATUS, default='P', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

 
    def save(self, *args, **kwargs):

        Order.objects.create()
        print('[CREATED] - A new order has been created')
        super(Payment, self).save(*args, **kwargs)
        
    def __str__(self): 
        return self.amount


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.reason}"