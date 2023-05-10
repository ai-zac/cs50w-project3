from django.db import models

# Create your models here.
class Users(models.Model):
    firts_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)


class ItemsType(models.Model):
    name = models.CharField(max_length=30)


class Items(models.Model):
    id_type = models.ForeignKey(ItemsType, on_delete=models.CASCADE)
    section = models.CharField(max_length=50)
    default_price = models.DecimalField(max_digits=5, decimal_places=2,default=0.0, null=True)
    second_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True)


class Carts(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items)


class Orders(models.Model):
    id_cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    order = models.BooleanField()

