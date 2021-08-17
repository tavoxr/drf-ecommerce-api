from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import ProductSerializer, CategorySerializer
from ..models import Product, Category


class CategoryDetail(APIView):

    def get_object(self,category_slug):
        try:
            return  Category.objects.get(slug= category_slug)
        except Category.DoesNotExist:
            return Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)