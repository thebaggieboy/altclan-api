from django.db import models
from django.conf import settings
from accounts.models import User
import uuid
from django.utils import timezone

from brands.models import BillingAddress

STATUS = (
    ('P', 'Pending'),
    ('C', 'Completed'),
)

# Create your models here.
class Order(models.Model): 
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    #address = models.ForeignKey(BillingAddress, on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{self.user} has made an active order!'


class Payment(models.Model):
    
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=250, choices=STATUS, default='P')

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Coupon(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Refund(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.id}"