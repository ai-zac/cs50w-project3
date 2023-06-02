from django.urls import include, path

from . import views

app_name = "orders"
urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/login", views.login, name="login"),
    path("accounts/register", views.register, name="register"),
]
