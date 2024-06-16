from django.urls import (
    include,
    path,
)

from shops import views


app_name = "shops"


urlpatterns = [
    path("shops/", views.GetShopListView.as_view(), name="shops"),
    path("address/", views.GetAddressListView.as_view(), name="address"),
]
