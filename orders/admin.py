from django.contrib import admin

from .models import MenuSection, Menu, Order, Cart, User
# Register your models here.
@admin.register(User)
class AllUser(admin.ModelAdmin):
    list_display = ("id", "firts_name", "last_name", "email")


@admin.register(Menu)
class AllMenu(admin.ModelAdmin):
    list_display = ("id", "section", "name")


@admin.register(MenuSection)
class AllType(admin.ModelAdmin):
    list_display = ("id", "section")


@admin.register(Order)
class AllOrder(admin.ModelAdmin):
    list_display = ("cart", "user")


