from django import forms
from django.core.validators import (MaxLengthValidator, MaxValueValidator,
                                    MinValueValidator)

from menu.models import Topping


class addItemForm(forms.Form):
    plate = forms.CharField(label="Your plate", disabled=True, initial="Valor")
    plate_id = forms.IntegerField(widget=forms.HiddenInput)
    item_id = forms.IntegerField(widget=forms.HiddenInput)
    amount = forms.IntegerField(label="Amount", initial=1)
    amount_toppings = forms.IntegerField(
        widget=forms.HiddenInput,
        validators=(MinValueValidator(limit_value=0), MaxValueValidator(limit_value=3)),
    )
