from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Products
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

# Create your views here.
class ProductListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])    
def get_featured_products(request):
    featured_products = Products.objects.filter(featured=True)
    serializer = ProductSerializer(featured_products, many=True)
    return Response({'featured_products': serializer.data})