from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class addItemForm(forms.Form):
    plate_id = forms.IntegerField(widget=forms.HiddenInput)
    price_id = forms.IntegerField(widget=forms.HiddenInput)
    amount = forms.IntegerField(label="Amount", initial=1)
    amount_toppings = forms.IntegerField(
        widget=forms.HiddenInput,
        validators=(MinValueValidator(limit_value=0), MaxValueValidator(limit_value=3)),
    )
