from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from menu.models import Price, Topping
from shopping.forms import addItemForm
from shopping.models import Cart, Order, PlatesInCart


@login_required(redirect_field_name="")
def show_my_orders(request):
    # Get user's cart items
    orders = Order.objects.filter(user=request.user).order_by("-id")

    context = {"orders": orders}

    return render(request, "shopping/myorders.html", context)


@login_required(redirect_field_name="")
def create_an_order(request, cart_id):
    # Change cart order status
    cart = get_object_or_404(Cart, id=cart_id)

    # Create new order with the cart and and its total price
    Order.add_new_order(request.user, cart, Cart.get_total_price(cart))

    # Then create a user's new cart
    Cart.create_new_cart(request.user)
    return HttpResponseRedirect(reverse("shopping:mycart"))


@login_required(redirect_field_name="")
def show_my_cart(request):
    # Get the current user cart, if not create a new one
    user_cart, created = Cart.objects.exclude(has_a_order=True).get_or_create(user=request.user)
    items_cart = PlatesInCart.objects.filter(cart=user_cart)

    context = {
        "cart_id": user_cart.id,
        "cart": items_cart,
    }

    return render(request, "shopping/mycart.html", context)


@login_required(redirect_field_name="")
@require_POST
def add_item_to_cart(request):
    """Save in the cart a string with the complete
    name of the plate and its toppings (if any)."""

    # Shorten "request.POST" in each line 
    form = request.POST

    # Add the form inputs (plate info.) as a name to the cart if valid
    f = addItemForm(form)
    if f.is_valid():
        full_name = ""

        # Add names of the plate and toppings (if any)
        # Plate name
        plate_price = Price.objects.get(pk=form["price_id"])
        full_name += plate_price.plate.name
        # Toppings name 
        for i in range(int(form["amount_toppings"])):
            try:
                full_name += " + "
                full_name += Topping.objects.get(pk=form[f"topping_{i}"]).name
            except KeyError:
                continue

        # Get user's cart, if there is no one without an order, create new one
        user_cart, created = Cart.objects.exclude(has_a_order=True).get_or_create(user=request.user)

        # Then add the complete item name in cart
        PlatesInCart.add_item(
            cart=user_cart,
            plate=plate_price,
            full_name=full_name,
            amount=int(form["amount"]),
            price=int(form["amount"]) * float(plate_price.price),
        )
    else:
        # For those who modify the HTML >:(
        return HttpResponseBadRequest("Gilipollas")

    # Then redirect to menu
    return HttpResponseRedirect(reverse("menu:index"))


@login_required(redirect_field_name="")
def show_add_form(request, plate_price_id):
    # Get plate's info
    plate_price = Price.objects.get(pk=plate_price_id)

    try:
        # Get amount of toppings available for the plate
        amount_toppings = plate_price.plate.toppings_available.get().amount
    except ObjectDoesNotExist:
        # If there is none, put 0
        amount_toppings = 0
        toppings = []
    else:
        # Else, just continue and get all toppings
        toppings = Topping.objects.all()

    # default form inputs
    input_default = {
        "plate": plate_price.plate.name,
        "plate_id": plate_price.plate.id,
        "price_id": plate_price.id,
        "amount_toppings": amount_toppings,
    }

    context = {
        "form": addItemForm(initial=input_default),
        "plate": plate_price,
        "toppings": toppings,
        "amount_toppings": amount_toppings,
    }

    return render(request, "shopping/cart.html", context)
