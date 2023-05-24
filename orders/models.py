from django.db import models

# Create your models here.
class User(models.Model):
    firts_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firts_name} {self.last_name}"


class MenuSection(models.Model):
    section = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.section}"


class Menu(models.Model):
    section = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.section} | {self.name}"


class ItemsWithToppings(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


class Topping(models.Model):
    topping = models.CharField(max_length=50)


class TypePrice(models.Model):
    type = models.CharField(max_length=15)


class Price(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    type = models.ForeignKey(TypePrice, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_yet = models.BooleanField(default=False)

    def __str__(self):
        return f"Cart: {self.id} <-> User: {self.user}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=80, blank=True)


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
