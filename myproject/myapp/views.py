from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

# Create your views here.
'''
@api_view()
def  product_list(request):
    return Response('OK')
'''


class ProductList(APIView):
    def get(self, request):
        myproducts = Product.objects.all()
        serializer = ProductSerializer(myproducts, many=True)
        return Response({"message": "Products retrieved successfully", "Data": serializer.data},  status=status.HTTP_200_OK)
   
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product created successfully", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error": "Product Creation Faild !", "details":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetails(APIView):

    def get(self, request, id):
        try:
            myproduct = Product.objects.get(id=id)
            serializer = ProductSerializer(myproduct)
            return Response({"message": "Product retive successfully",  "Data": serializer.data}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"Eror": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    
