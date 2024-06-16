from products.models import Product, BestProduct
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'last_price', 'discount', 'img_url', 'shop']


class CreateBestProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)
    telegram_id = serializers.IntegerField(write_only=True)

    def validate(self, data):
        product_id = data.get('product_id')
        telegram_id = data.get('telegram_id')
        try:
            Product.objects.get(pk=product_id)
        except:
            raise serializers.ValidationError("Product does not exist")

        best_product = BestProduct.objects.filter(telegram_id=telegram_id).first()
        if best_product:
            raise serializers.ValidationError("BestProduct with this telegram_id already exists")

        return data

    def create(self, validated_data):
        product_id = validated_data.get('product_id')
        telegram_id = validated_data.get('telegram_id')
        product = Product.objects.get(pk=product_id)
        best_product = BestProduct.objects.create(product=product, telegram_id=telegram_id)
        return {
            "message": "BestProduct created",
            "best_product_id": best_product.id
        }

    class Meta:
        model = BestProduct
        fields = '__all__'
