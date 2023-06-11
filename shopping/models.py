from django.contrib.auth.models import User
from django.db import models

from menu.models import Plate

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plates = models.ManyToManyField(Plate, through="PlatesInCart")
    has_a_order = models.BooleanField(default=False)

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
