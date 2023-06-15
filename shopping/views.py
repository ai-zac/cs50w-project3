from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.utils.translation import gettext_lazy as _

from menu.models import Price, Topping
from shopping.forms import addItemForm
from shopping.models import Cart, PlatesInCart

@login_required
def mycart(request):
    user_cart, created = Cart.objects.exclude(has_a_order=True).get_or_create(user=request.user)

    context = {
        "cart": user_cart
    }

    return render(request, "shopping/mycart.html", context)

@login_required
@require_POST
def add(request):
    """Save in the cart a string with the complete
    name of the plate and its toppings (if any)."""

    # It is just to shorten the name of request.POST in each line.
    form = request.POST

    # Save the info if plate's name and amount are valid
    f = addItemForm(form)
    if f.is_valid():
        full_name = ""

        # Add user's selected plate & toppings to full_name
        item = Price.objects.get(pk=form["item_id"])
        full_name += item.plate.name
        for i in range(int(form["amount_toppings"])):
            try:
                # Add toppings to the full_name if they exist
                full_name += " + "
                full_name += Topping.objects.get(pk=form[f"topping_{i}"]).name
            except KeyError:
                continue

        # Get current cart, if none exists without an order, create new one
        user_cart, created = Cart.objects.exclude(has_a_order=True).get_or_create(user=request.user)

        # Then save item's full_name in the cart
        add = PlatesInCart(
            cart=user_cart,
            plate=item,
            full_name=full_name,
            amount=int(form["amount"])
        )
        add.save()
    else:
        # For those who modify the HTML >:(
        return HttpResponseBadRequest("Gilipollas") 

    # Then redirect to menu
    return HttpResponseRedirect(reverse("menu:index"))


@login_required
def show_plates_form(request, plate_price_id):
    # Get plate's info
    item = Price.objects.get(pk=plate_price_id)

    try:
        # Get amount of toppings available for the form
        amount_toppings = item.plate.toppings_available.get().amount
    except ObjectDoesNotExist:
        # If there is none, put 0
        amount_toppings = 0
        toppings = []
    else:
        # Else, just continue and get all toppings
        toppings = Topping.objects.all()

    # default form inputs
    # idk wtf doing with this
    input_default = {
        "plate": item.plate.name,
        "plate_id": item.plate.id,
        "item_id": item.id,
        "amount": 1,
        "amount_toppings": amount_toppings
    }

    context = {
        "form": addItemForm(initial=input_default),
        "plate": item,
        "toppings": toppings,
        "amount_toppings": amount_toppings,
    }

    return render(request, "shopping/cart.html", context)
