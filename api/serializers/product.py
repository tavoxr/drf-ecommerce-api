from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model =  Product
        fields = (
            "id",
            "name",
            "price",
            "description",
            "get_absolute_url",
            "get_image",
            "get_thumbnail"
        )
