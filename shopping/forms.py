from django import forms
from menu.models import Topping


class addItemForm(forms.Form):
    TOPPINGS = []
    for topping in Topping.objects.all():
        TOPPINGS.append((topping.id, topping.name))

    item = forms.CharField(label='Your plate', disabled=True, initial="Valor")
    item_id = forms.IntegerField(widget=forms.HiddenInput)
    amount = forms.IntegerField(label='Amount', initial=1)
