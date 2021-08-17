from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Product
from ..serializers import ProductSerializer

@api_view(['POST'])
def search(request):
    query =  request.data.get('query','')

    print('request.data', request.data)

    if query:
        products = Product.objects.filter(Q(name__icontains = query) | Q(description__icontains = query))
        serializer = ProductSerializer(products, many = True)
        return Response(serializer.data)
        
    else:
        return Response({"products": []})