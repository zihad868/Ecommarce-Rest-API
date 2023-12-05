from rest_framework import serializers
from django.utils.text import slugify

from .models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = {'id': instance.category.id, 'title': instance.category.title,
                               'slug': instance.category.slug}
        return context

    def update(self, instance, validated_data):
        context = super().update(instance, validated_data)
        context.slug = slugify(context.title)
        context.save()
        return context


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductRetriveSerializer(serializers.ModelSerializer):
    related_products = serializers.SerializerMethodField(method_name='get_related_product')

    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'slug', 'featured', 'thumbnail', 'price', 'description',
                  'related_products']

    def to_representation(self, instance):
        context = super().to_representation(instance)

        context['category'] = {'id': instance.category.id, 'title': instance.category.title,
                               'slug': instance.category.slug}
        return context

    def get_related_product(self, obj):
        return ProductSerializer(obj.related, many=True).data


class CategoryRetriveSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField(method_name='get_category')

    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'featured', 'categories', 'created_date']

    def get_category(self, obj):
        return ProductSerializer(obj.products.all(), many=True).data
