from django.contrib import admin
from .models import Category, Product, BestProduct


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(BestProduct)
class BestProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product")
    readonly_fields = ("product", "telegram_id")


admin.site.register(Category)
