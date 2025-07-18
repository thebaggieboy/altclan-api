from django.db import models
from django.conf import settings
from accounts.models import User
import uuid
from django.utils import timezone
import uuid
from django.utils.crypto import get_random_string
from brands.models import BillingAddress
from django.utils.text import slugify
from django.contrib.postgres.fields import ArrayField

STATUS = (
    ('P', 'Pending'),
    ('C', 'Completed'),
)

DEPOSIT_TYPE = (
    ('Transfer', 'Transfer'),
    ('Card', 'Card'),
    ('USSD', 'USSD'),
)
BILLING_TYPE = (
    ('Monthly', 'Monthly'),
    ('Yearly', 'Yearly'),
    
)

User = settings.AUTH_USER_MODEL
RANDOM_ORDER_ID = get_random_string(length=12)


class Accounts(models.Model):
    bank_name = models.CharField(max_length=15, default='', null=True)
    bank_code = models.CharField(max_length=15, default='', null=True)
    account_name = models.CharField(max_length=15, default='', null=True)
    account_number = models.CharField(max_length=15, default='', null=True)

    def __str__(self):
        return self.bank_code

class Deposit(models.Model):

    amount = models.FloatField()

    def __str__(self):
        return self.code

class Withdraw(models.Model):
    amount = models.FloatField()

    def __str__(self):
        return self.code


class Cards(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='user_cards')
    card_holder = models.CharField(max_length=250,  default='', null=True)
    card_number = models.CharField(max_length=20, default='', null=True)
    expiry_date = models.CharField(max_length=15, default='', null=True)
    cvv = models.CharField(max_length=15, default='', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.card_holder
class Order(models.Model): 

    name_of_item = models.CharField(max_length=250, blank=True)
    user_email = models.CharField(max_length=250, blank=True)
    name_of_brand = models.CharField(max_length=250, blank=True)
    amount_per_item = models.CharField(max_length=250, blank=True)
    total_amount = models.IntegerField()
    quantity = models.CharField(max_length=250, blank=True)
    tracking_number = models.CharField(max_length=250, default=get_random_string(length=12))
    number_of_items = models.IntegerField(null=True)
    address = models.CharField(max_length=250, blank=True)
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(default=timezone.now())
    item = ArrayField(models.CharField(max_length=250, null=True, blank=True), default=list)  
      
    

    def __str__(self):
        return f'{self.tracking_number}'

class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name='user_order')
    paystack_reference_number = models.CharField(max_length=250, blank=True, null=True)
    customer = models.CharField(max_length=250, blank=True, null=True)

    payment_method = models.CharField(max_length=250, blank=True, null=True)    
    amount = models.FloatField()
    status = models.CharField(max_length=250, null=True, blank=True)
    order_id = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

 
    def save(self, *args, **kwargs):

        
        print('[CREATED] - A new payment has been made')
        super(Payment, self).save(*args, **kwargs)
        
    def __str__(self): 
        return self.amount
class Billing(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name='user_billing')
    billing_period = models.CharField(max_length=250, blank=True, null=True)
    payment_method = models.CharField(max_length=250, blank=True, null=True) 
    card = models.ForeignKey(Cards, on_delete=models.CASCADE, null=True, blank=True)   
    invoice_id = models.CharField(max_length=250, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    renewal_date = models.DateTimeField()
 
    def save(self, *args, **kwargs):

        
        print('[CREATED] - A new billing information has been created')
        super(Payment, self).save(*args, **kwargs)
        
    def __str__(self): 
        return self.timestamp


class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()

    def __str__(self):
        return self.code

class BillingSettings(models.Model):
    billing_period = models.CharField(max_length=15)
    payment_method = models.CharField(max_length=15)

    def __str__(self):
        return self.biling_period


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    email = models.EmailField()

    def __str__(self):
        return f"{self.reason}"