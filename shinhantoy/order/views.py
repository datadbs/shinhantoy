from django.shortcuts import render
from rest_framework import mixins, generics

from .serializers import OrderSerializer
from .models import Order
# Create your views here.

class OrderListView(
    mixins.ListModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        orders = Order.objects.all()
        return orders

    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class OrderDetailView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    serializer_class = OrderSerializer

    def get_queryset(self):
        orders = Order.objects.all()
        return orders

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)