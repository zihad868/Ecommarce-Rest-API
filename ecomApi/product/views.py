from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from . models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

class ListProduct(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    #queryset = Product.objects.order_by('-id')
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.order_by('-id')


class ListCategory(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer