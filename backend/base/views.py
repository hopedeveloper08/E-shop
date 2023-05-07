from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductsAPI(APIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductAPI(APIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        product = Product.objects.get(_id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class CategoryAPI(APIView):
    # permission_classes = (IsAuthenticated, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        product = Product.objects.all()
        counter = 0
        categorys = []
        for c in product:
            if c.category not in categorys:
                categorys.append(c.category)
        return Response({'categorys': categorys})
