from django.db import models
from parsing.models import ParsingSetting
from shops.models import Shop


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):

    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    settings = models.ForeignKey(ParsingSetting, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True, null=True)
    img_url = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True, blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    validity_date = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class BestProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    telegram_id = models.IntegerField(unique=True)

