from django.shortcuts import render
from django.conf import settings
from rest_framework import viewsets
 
from .models import  WishList, Merchandise, Leads

from .serializers import *

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    #order_by = ['date_created']


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all().order_by('-date_created').values()
    serializer_class = MerchandiseSerializer
    #order_by = ['date_created']


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


def create_merchandise_list(request):

    return render(request, 'alteclan/index.html')