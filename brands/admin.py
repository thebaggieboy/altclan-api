from django.contrib import admin
from .models import Merchandise, Cart,  BillingAddress
from reviews.models import Reviews
from accounts.models import BrandProfile

class BrandProfileInline(admin.TabularInline):
    model = BrandProfile
    extra = 3


class BrandProfileAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['id', 'user', 'date_created',]
    list_filter = ['date_created']


class MerchandiseAdmin(admin.ModelAdmin):
    #inlines = [BrandInline]
    list_display = ['brand_name', 'merchandise_name', 'merchandise_color', 'merchandise_size', 'display_image', 'labels',  'price', 'delivery_cost', 'slug']
    list_filter = ['date_created']

class BillingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'street_address', 'city', 'state', 'zip']



admin.site.register(BillingAddress, BillingAddressAdmin)
admin.site.register(BrandProfile, BrandProfileAdmin)
admin.site.register(Merchandise, MerchandiseAdmin)
admin.site.register(Cart)
admin.site.register(Reviews)




