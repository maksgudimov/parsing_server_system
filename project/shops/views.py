from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from shops.models import Shop, City, Address
from shops.serializers import ShopSerializer, ShopSerializerAddress


# Create your views here.


class GetShopListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


# class GetAddressListView(ListAPIView):
#     permission_classes = [IsAuthenticated]
#
#     queryset = Address.objects.all()
#     serializer_class = AddressSerializer


class GetAddressListView(ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Shop.objects.all()
    serializer_class = ShopSerializerAddress