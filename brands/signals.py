from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import BrandProfile
from .models import Brand, Merchandise


# If a new MErchandise is created, silmultaneously create a .. for the merch.


