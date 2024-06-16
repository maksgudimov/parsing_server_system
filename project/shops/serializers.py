from shops.models import Shop, Address, City
from rest_framework import serializers


class GroupedAddressSerializer(serializers.Serializer):
    city = serializers.CharField()
    streets = serializers.ListField(child=serializers.CharField())


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', ]


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class AddressSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Address
        fields = ['street', 'city']


class ShopSerializerAddress(serializers.ModelSerializer):
    address = AddressSerializer(many=True)

    class Meta:
        model = Shop
        fields = ['name', 'address']
