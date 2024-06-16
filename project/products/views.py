from django.db.models import Count
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from products.models import Product, BestProduct
from products.serializers import ProductSerializer, CreateBestProductSerializer
from products.paginations import PaginatedOneList
from rest_framework import status


# class ProductsView(ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     pagination_class = PaginatedOneList
#


class ProductsView(ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PaginatedOneList
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            shop_id = int(self.request.query_params.get('shop_id'))
            if shop_id is not None:
                return Product.objects.filter(shop_id=shop_id)
            else:
                return Product.objects.none()
        except Exception as exp:
            print(exp)
            return Product.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductShopList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]


class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductBest(CreateAPIView, RetrieveAPIView):
    serializer_class = CreateBestProductSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return CreateBestProductSerializer

    def get(self, request, *args, **kwargs):
        most_popular_product = BestProduct.objects.values('product_id') \
            .annotate(count=Count('product_id')) \
            .order_by('-count') \
            .first()

        if most_popular_product:
            product_id = most_popular_product['product_id']
            product = Product.objects.get(id=product_id)
            serializer = self.get_serializer(product)
            best_product = serializer.data
            BestProduct.objects.all().delete()
            return Response(best_product, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "No popular products found."}, status=status.HTTP_404_NOT_FOUND)






