from rest_framework import serializers
from .product import ProductSerializer
from ..models import Category


class CategorySerializer(serializers.ModelSerializer):
    products =  ProductSerializer(many=True)
    
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "products",
        )