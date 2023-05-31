from django.contrib.auth.models import User
from django.db import models
from django.template.response import select_template


# Create your models here.
class MenuSection(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"


class Plate(models.Model):
    section = models.ForeignKey(
        MenuSection, on_delete=models.CASCADE, related_name="plates"
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.section})"


class PlatesWithTopping(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.plate} has {self.amount} topping(s) aviable"


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class TypePrice(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.category}"


class Price(models.Model):
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    category = models.ForeignKey(TypePrice, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.plate} = {self.category} price to ${self.price}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    has_a_order = models.BooleanField(default=False)
    plates = models.ManyToManyField(Plate, through="PlatesInCart")

    def __str__(self):
        return f"{self.user}'s cart{self.id}"


class PlatesInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"{self.cart} has {self.full_name}"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart} has a order"
