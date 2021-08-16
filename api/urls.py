from os import name
from django.urls import path, include
from .views import *

urlpatterns = [
    path('latest-products/', LatestProductsList.as_view(), name="latest-products"),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view(), name="productDetail"),
    

]