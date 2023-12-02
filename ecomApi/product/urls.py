from django.urls import path

from .views import ListProduct, ListCategory, RetrieveProduct, RetriveCategory

urlpatterns = [
    path('list-product/', ListProduct.as_view(), name='list-product'),
    path('list-category/', ListCategory.as_view(), name='list-category'),
    path('retrive-product/<str:slug>/', RetrieveProduct.as_view(), name='retrive-product'),
    path('retrive-category/<str:slug>/', RetriveCategory.as_view(), name="retrive-category")
]
