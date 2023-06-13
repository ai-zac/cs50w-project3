from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST

from menu.models import Plate, Topping
from shopping.forms import addItemForm


@login_required
@require_POST
def add(request):
    form = addItemForm(request.POST)
    if form.is_valid():
        print("Valid")

    # create cart for user if exists
    # else just get the current cart
    # then add the current plate (id, name)
    # Problems: 
    #   1- The current "is_valid" run when only send
    #       a plate with no toppings, resolve that
    return HttpResponseRedirect(reverse("menu:index"))


@login_required
def show_plates_form(request, plate_id):
    # Get plate's info
    plate = Plate.objects.get(pk=plate_id)

    try:
        # Get amount of toppings available for the form
        amount_available_toppings = plate.toppings_available.get().amount
    except ObjectDoesNotExist:
        # If there is none, put 0
        amount_available_toppings = 0
        toppings = []
    else:
        # Else, just continue and get all toppings
        toppings = Topping.objects.all()

    # default form inputs
    input_default = {
        "item": plate.name,
        "item_id": plate.id,
        "amount": 1,
    }

    context = {
        "form": addItemForm(initial=input_default),
        "plate": plate,
        "toppings": toppings,
        "amount_available_toppings": amount_available_toppings,
    }

    return render(request, "shopping/cart.html", context)
