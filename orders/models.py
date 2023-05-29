from django.db import models

# Create your models here.
class User(models.Model):
    firt_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firt_name} {self.last_name}"


class ItemSection(models.Model):
    section_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.section_name}"


class Item(models.Model):
    section_name = models.ForeignKey(ItemSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.section_name} | {self.name}"


class ItemsWithToppings(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.item} <-> {self.amount} topping(s)"


class Topping(models.Model):
    topping = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.topping}"


class TypePrice(models.Model):
    category = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.category}"


class Price(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    category = models.ForeignKey(TypePrice, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.item}: price {self.category} ${self.price}"


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    items = models.ManyToManyField(Item, through="CartItem")

    def __str__(self):
        return f"{self.user}'s cart{self.id}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"{self.cart} <- {self.item} ({self.item_name})"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
