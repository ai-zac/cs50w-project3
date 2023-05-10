from django.contrib import admin

from .models import ItemType, Item
# Register your models here.
@admin.register(Item)
class AllItem(admin.ModelAdmin):
    list_display = ("id", "id_type", "name", "default_price", "second_price")

@admin.register(ItemType)
class AllType(admin.ModelAdmin):
    list_display = ("id", "name")
