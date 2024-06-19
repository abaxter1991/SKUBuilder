from datetime import datetime

from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins

from .faire import my_faire_store
from .models import SalesOrder
from .serializers import SalesOrderSerializer


def sales(request):
    context = {}

    return render(request, 'sales/sales.html', context)


def faire_api(request):
    faire_orders = my_faire_store()
    db_orders = SalesOrder.objects.all()

    def format_date(faire_datetime):
        date, _ = faire_datetime.split('T')
        date = datetime.strptime(date, '%Y%m%d').date()

        return date

    for order in faire_orders['orders']:
        order['products'] = order['items']
        del order['items']

        order['created_at'] = format_date(order['created_at'])
        order['updated_at'] = format_date(order['updated_at'])

    context = {
        'faire_orders': faire_orders,
        'db_orders': db_orders
    }

    return render(request, 'sales/faire.html', context)


class SalesOrderAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView):

    serializer_class = SalesOrderSerializer
    queryset = SalesOrder.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SalesOrderListAPIView(generics.ListAPIView):
    serializer_class = SalesOrderSerializer
    queryset = SalesOrder.objects.all()


class SalesOrderCreateAPIView(generics.CreateAPIView):
    serializer_class = SalesOrderSerializer
    queryset = SalesOrder.objects.all()


class SalesOrderUpdateAPIView(generics.UpdateAPIView):
    serializer_class = SalesOrderSerializer
    queryset = SalesOrder.objects.all()


class SalesOrderDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SalesOrderSerializer
    queryset = SalesOrder.objects.all()
