from django.contrib import admin

from .models import Cart, Order, PlatesInCart


# Register your models here.
@admin.register(Order)
class Orders(admin.ModelAdmin):
    list_display = ("cart",)


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ("id", "user", "has_a_order")


@admin.register(PlatesInCart)
class PlatesInCart(admin.ModelAdmin):
    list_display = ("cart", "plate", "full_name", "amount")
