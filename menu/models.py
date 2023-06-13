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
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE, related_name="toppings_available")
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.plate} has {self.amount} topping(s) available"


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Price(models.Model):
    PRICES_CATEGORY = [
        ("Normal", "Normal"),
        ("Small", "Small"),
        ("Large", "Large"),
    ]
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    category = models.CharField(max_length=6, choices=PRICES_CATEGORY)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.plate} = {self.category} price to ${self.price}"
