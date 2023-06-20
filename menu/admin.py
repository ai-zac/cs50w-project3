from django.contrib import admin

from .models import Plate, PlatesWithTopping, Price, Topping, Section


# Register your models here.
@admin.register(Plate)
class Plates(admin.ModelAdmin):
    list_display = ("id", "section", "name")


@admin.register(Topping)
class Toppings(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(PlatesWithTopping)
class PlatesWithToppings(admin.ModelAdmin):
    list_display = ("id", "plate", "amount")


@admin.register(Price)
class Prices(admin.ModelAdmin):
    list_display = ("id", "plate", "category", "price")


@admin.register(Section)
class Sections(admin.ModelAdmin):
    list_display = ("id", "title")
