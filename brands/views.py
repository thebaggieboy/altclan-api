from django.shortcuts import render
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.conf import settings
from rest_framework import viewsets
 
from .models import  WishList, Merchandise, Leads

from .serializers import *

class WishListViewSet(viewsets.ModelViewSet):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    #order_by = ['date_created']


@method_decorator(cache_page(300), name='list')
@method_decorator(cache_page(300), name='retrieve')
@method_decorator(vary_on_headers('Cookie', 'Authorization'), name='list')
class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all().order_by('-date_created').values()
    serializer_class = MerchandiseSerializer
    #order_by = ['date_created']


class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer


def create_merchandise_list(request):

    return render(request, 'alteclan/index.html')