from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from menu.models import Plate, Topping

from shopping.forms import addItemForm

@login_required
@require_POST
def add(request):
    return HttpResponseRedirect(reverse("menu:index"))  



@login_required
def show_plates_form(request, plate_id):
    plate = Plate.objects.get(pk=plate_id)

    try:
        amount_aviable_toppings = plate.toppings_aviable.get().amount
        toppings = Topping.objects.all()
    except: 
        amount_aviable_toppings = 0
        toppings = []

    context = {
        "id": plate_id,
        "form": addItemForm(),
        "plate": plate,
        "amount_aviable_toppings": amount_aviable_toppings,
        "toppings": toppings
    }

    return render(request, "shopping/cart.html", context)
