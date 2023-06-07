from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path("mycart/add/<int:plate_id>", views.add_to_cart, name="adding"),
]
