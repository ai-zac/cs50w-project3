from django.contrib.auth.models import User
from django.db import models
from django.utils.module_loading import module_dir

from menu.models import Price


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plates = models.ManyToManyField(Price, through="PlatesInCart", through_fields=("cart", "plate"))
    has_a_order = models.BooleanField(default=False)

    @classmethod
    def get_total_price(cls, cart_id):
        # Get cart plates
        items = PlatesInCart.objects.filter(cart=cart_id)

        # Get total cart price
        total_price = 0.0
        for item in items:
            total_price += float(item.plate.price) * item.amount
        return total_price

    def __str__(self):
        return f"{self.user}'s cart{self.id}"


class PlatesInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    plate = models.ForeignKey(Price, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=80, blank=True)
    amount = models.IntegerField(default=0)
    price = models.DecimalField(default=0, max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.cart} has {self.full_name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=4)

    def __str__(self):
        return f"{self.cart} has a order"
