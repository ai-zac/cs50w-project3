from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("mycart/", views.mycart, name="mycart"),
    path("mycart/add/", views.add, name="add"),
    path("mycart/add/<int:plate_price_id>", views.show_plates_form, name="adding"),
    path("myorders/", views.myorders, name="myorders"),
    path("myorders/create/<int:cart_id>", views.createOrder, name="createorder")
]
