from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from menu.models import Plate

from shopping.forms import addItemForm


@login_required
def add_to_cart(request, plate_id):
    if request.method == "POST":
        return HttpResponseRedirect(reverse("menu:index"))

    context = {
        "id": plate_id,
        "form": addItemForm(),
        "plate": Plate.objects.get(pk=plate_id),
    }
    return render(request, "shopping/cart.html", context)
    
