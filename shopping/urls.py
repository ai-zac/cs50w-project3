from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("mycart/", views.show_my_cart, name="mycart"),
    path("mycart/add/", views.add_item_to_cart, name="additem"),
    path("mycart/add/<int:plate_price_id>", views.show_add_form, name="addform"),
    path("myorders/", views.show_my_orders, name="myorders"),
    path("myorders/create/<int:cart_id>", views.create_an_order, name="createorder")
]
