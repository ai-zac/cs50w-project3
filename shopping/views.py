from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, plate_id):
    return render(request, "shopping/cart.html", {"id": plate_id})
