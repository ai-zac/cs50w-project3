from django.urls import path

from . import views

app_name = "shopping"
urlpatterns = [
    path("mycart/add/", views.add, name="add"),
    path("mycart/add/<int:plate_id>", views.show_plates_form, name="adding"),
]
