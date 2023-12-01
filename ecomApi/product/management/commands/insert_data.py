from django.core.management.base import BaseCommand, CommandError
import requests
from django.utils.text import slugify
from product.models import Category, Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Creating Data.......")
        response = requests.get("https://fakestoreapi.com/products").json()
        
        for product in response:
            category, _ = Category.objects.get_or_create(
                title = product['title'],
                slug = slugify(product['title'])
            )
            
            Product.objects.get_or_create(
                category = category,
                title = product['title'],
                slug = slugify(product['title']),
                price = product['price'],
                thumbnail = product['image'],
                description = product['description']
            )
            
        print("Complete Data")