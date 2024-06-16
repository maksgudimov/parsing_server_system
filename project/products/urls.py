from django.urls import (
    include,
    path,
)

from products import views


app_name = "products"


urlpatterns = [
    path("", views.ProductsView.as_view(), name="products"),
    path("all/", views.ProductShopList.as_view(), name="products-all"),
    path("<int:pk>/", views.ProductDetail.as_view(), name="products-detail"),
    path("best/", views.ProductBest.as_view(), name="products-best"),

]