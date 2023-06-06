from django.urls import path

from . import views

app_name = "orders"
urlpatterns = [
    path("", views.index, name="index"),
    path("accounts/", views.accounts, name="accounts"),
    path("accounts/register/", views.register, name="register"),
    path("accounts/login/", views.login, name="login"),
    path("accounts/logout/", views.logout, name="logout"),
]
