from django.contrib import admin

from .models import (Cart, CartItem, Item, ItemSection, ItemsWithToppings,
                     Order, Price, Topping, TypePrice, User)


# Register your models here.
@admin.register(User)
class Users(admin.ModelAdmin):
    list_display = ("id", "firt_name", "last_name", "email")


@admin.register(Item)
class Items(admin.ModelAdmin):
    list_display = ("id", "section", "name")


@admin.register(Topping)
class Toppings(admin.ModelAdmin):
    list_display = ("topping",)


@admin.register(ItemsWithToppings)
class ItemsWithToppings(admin.ModelAdmin):
    list_display = ("item", "amount")


@admin.register(Price)
class Prices(admin.ModelAdmin):
    list_display = ("item", "category", "price")


@admin.register(TypePrice)
class TypePrices(admin.ModelAdmin):
    list_display = ("category",)


@admin.register(ItemSection)
class Sections(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Order)
class Orders(admin.ModelAdmin):
    list_display = ("cart",)


@admin.register(Cart)
class Cart(admin.ModelAdmin):
    list_display = ("id", "user", "status")


@admin.register(CartItem)
class ItemsInCart(admin.ModelAdmin):
    list_display = ("cart", "item", "item_name")
