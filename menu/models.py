from django.db import models

# Create your models here.
class Section(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"


class Plate(models.Model):
    section = models.ForeignKey(
        Section, on_delete=models.CASCADE, related_name="plates"
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
