from django.urls import path

from .views import ListProduct, ListCategory

urlpatterns = [
    path('list-product', ListProduct.as_view(), name='list-product'),
    path('list-category', ListCategory.as_view(), name='list-category'),
]
