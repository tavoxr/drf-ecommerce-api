from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import ProductSerializer
from ..models import Product

class LatestProductsList(APIView):

    def get(self, request, format=None):

        products = Product.objects.all()[0:5]
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
