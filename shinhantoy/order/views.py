from django.shortcuts import render
from rest_framework import mixins, generics

from .serializers import OrderSerializer, CommentSerializer, CommentCreateSerializer, CommentDeleteSerializer
from .models import Order, Comment
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



class CommentListView(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                .select_related('user', 'order') \
                .order_by('-id')
        return Comment.objects.none()

    def get(self,request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)


class CommentCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView
):  
    serializer_class = CommentCreateSerializer

    def get_queryset(self):
        order_id = self.kwargs.get('order_id')
        if order_id:
            return Comment.objects.filter(order_id=order_id) \
                .select_related('user', 'order') \
                .filter()
        return Comment.objects.none()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    

class CommentDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    serializer_class = CommentDeleteSerializer
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk:
            return Comment.objects.filter(pk=pk) \
                .select_related('user', 'order') \

        return Comment.objects.none()

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)