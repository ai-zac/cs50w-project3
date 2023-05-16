from django.db import models

# Create your models here.
class User(models.Model):
    firts_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firts_name} | {self.last_name}"


class MenuSection(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    id_section = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id_section} | {self.name}"


class PizzasMenu(models.Model):
    id_section = models.ForeignKey(MenuSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Menu)


class Topping(models.Model):
    topping = models.CharField(max_length=50)


class TypePrice(models.Model):
    type = models.CharField(max_length=15)


class Price(models.Model):
    id_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    id_type = models.ForeignKey(TypePrice, on_delete=models.CASCADE)
    default_price = models.DecimalField(max_digits=5, decimal_places=2,default=0.0, null=True)


class Cart(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Menu)


class Order(models.Model):
    id_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.BooleanField()

