from django.db.models.signals import post_save
from django.dispatch import receiver

 
from .models import  Merchandise


# If a new MErchandise is created, silmultaneously create a .. for the merch.


