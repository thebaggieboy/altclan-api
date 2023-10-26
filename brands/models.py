import uuid
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from .display import LABEL_DISPLAY, COLLECTION_DISPLAY, COMMUNITY_TYPE_DISPLAY
from django.conf import settings
from account.models import BrandProfile

User = settings.AUTH_USER_MODEL
BrandUser = settings.BRAND_USER_MODEL

from .choices import STATUS, GENDER, COMMUNITY_TYPE, CLOTHING_CATEGORY
from account.models import BrandProfile

class BrandDashboard(models.Model):
    #user = models.OneToOneField(BrandUser, on_delete=models.CASCADE, related_name='brand_dashboard', null=True, blank=True)
    profile = models.OneToOneField(BrandProfile, on_delete=models.CASCADE, related_name='brand_dashboard', null=True, blank=True)
    total_views = models.CharField(max_length=250, null=True, blank=True)
    total_users = models.CharField(max_length=250, null=True, blank=True)
    total_products = models.CharField(max_length=250, null=True, blank=True)
    total_profit = models.CharField(max_length=250, null=True, blank=True)
    total_revenue = models.CharField(max_length=250, null=True, blank=True)
    total_sales = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return f'{self.user} Dashboard'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.user = slugify(f'{self.user}')
        return super().save(*args, **kwargs)



class Merchandise(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    brand = models.ForeignKey(BrandUser, on_delete=models.CASCADE,  null=True, blank=True)
    merchandise_name = models.CharField(max_length=250, default='')
    merchandise_color = models.CharField(max_length=250, default='')
    merchandise_size = models.CharField(max_length=250, default='')
    display_image = models.ImageField(upload_to='Merch Image', default='')
    available_color_1 = models.CharField(max_length=250, null=True, blank=True)
    available_color_2 = models.CharField(max_length=250, null=True, blank=True)
    available_color_3 = models.CharField(max_length=250, null=True, blank=True)
    image_1 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)
    image_2 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)
    image_3 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)
    image_4 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)
    image_5 = models.ImageField(upload_to='Merch Image', default='', null=True, blank=True)
    labels = models.CharField(max_length=250, choices=LABEL_DISPLAY, default='')
    price = models.CharField(max_length=250, default='')
    delivery_cost = models.CharField(max_length=250, default='', null=True, blank=True)
    discount = models.CharField(max_length=250, default='', null=True, blank=True)
    category = models.CharField(choices=CLOTHING_CATEGORY, default='', null=True, blank=True, max_length=250)
    slug = models.SlugField()
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'Merchandise Name : {self.merchandise_name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.id}')
        return super().save(*args, **kwargs)


class Leads(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    brand_name = models.CharField(max_length=250, null=True, blank=True)
    instagram_username = models.CharField(max_length=250, null=True, blank=True)
    website_link = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, default='')
    def __str__(self):
        return f'Brands Leads'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.brand_name}')
        return super().save(*args, **kwargs)
# ProductOrder, these are the items that have been
class BillingAddress(models.Model):
    
    user = models.OneToOneField(BrandUser, on_delete=models.CASCADE, related_name='address', null=True, blank=True)
    street_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'{self.user}'
    
class UserBillingAddress(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_address', null=True, blank=True)
    street_address = models.CharField(max_length=250, default='')
    city = models.CharField(max_length=250, default='')
    state = models.CharField(max_length=250, default='')
    zip = models.CharField(max_length=250, default='')

    def __str__(self):
        return f'{self.user}'    
# Inherits from brand


class Cart(models.Model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    merchandises = models.ManyToManyField(Merchandise)
    address = models.ForeignKey('BillingAddress', on_delete=models.CASCADE, null=True, blank=True, )
    # Inherit order and bring it into the cart
    # Show list of orders and their quantities

    def __str__(self):
        return f'{self.merchandises} x ( {self.quantity} ) pcs by {self.user} '

# Represent a particular product order
