from django import forms
from menu.models import Topping


class addItemForm(forms.Form):
    TOPPINGS = []
    for topping in Topping.objects.all():
        TOPPINGS.append((topping.id, topping.name))

    item = forms.CharField(label='Your plate')
    amount = forms.CharField(label='Amount')
    item1 = forms.ChoiceField(label='item No.1', choices=TOPPINGS)
    item2 = forms.ChoiceField(label='item No.2', choices=TOPPINGS)
    item3 = forms.ChoiceField(label='item No.3', choices=TOPPINGS)
