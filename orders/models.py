from django.db import models

# Create your models here.
class User(models.Model):
    firts_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)


class ItemType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}: {self.name}"


class Item(models.Model):
    id_type = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    default_price = models.DecimalField(max_digits=5, decimal_places=2,default=0.0, null=True)
    second_price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, null=True)

    def __str__(self):
        return f"ID={self.id}; TYPE_ID={self.id_type}; name={self.name}; default_price={self.default_price}; second_price={self.second_price}"

class Cart(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)


class Order(models.Model):
    id_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order = models.BooleanField()

