from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions

from . models import Product, Category
from .serializers import  ProductSerializer, CategorySerializer, ProductRetriveSerializer, CategoryRetriveSerializer

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


class RetrieveProduct(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductRetriveSerializer
    lookup_field = 'slug'
    

class RetriveCategory(generics.RetrieveAPIView):
    parser_classes = [permissions.AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategoryRetriveSerializer
    lookup_field = 'slug'
    