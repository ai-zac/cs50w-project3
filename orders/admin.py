from django.contrib import admin

from .models import (Cart, MenuSection, Order, Plate, PlatesInCart,
                     PlatesWithTopping, Price, Topping, TypePrice)


# Register your models here.
@admin.register(Plate)
class Plates(admin.ModelAdmin):
    list_display = ("id", "section", "name")


@admin.register(Topping)
class Toppings(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(PlatesWithTopping)
class PlatesWithToppings(admin.ModelAdmin):
    list_display = ("plate", "amount")


@admin.register(Price)
class Prices(admin.ModelAdmin):
    list_display = ("plate", "category", "price")


@admin.register(TypePrice)
class TypePrices(admin.ModelAdmin):
    list_display = ("category",)


@admin.register(MenuSection)
class Sections(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Order)
class Orders(admin.ModelAdmin):
    list_display = ("cart",)


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ("id", "user", "has_a_order")


@admin.register(PlatesInCart)
class PlatesInCart(admin.ModelAdmin):
    list_display = ("cart", "plate", "full_name")
