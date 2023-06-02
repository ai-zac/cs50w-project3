from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Plate


# Create your views here.
def index(request):
    context = {
        "Menu": Plate.objects.all(),
    }
    return render(request, "orders/index.html", context)


def register(request):
    inputs = request.POST
    context = {
        "UserCreationForm": UserCreationForm(),
        "isValid": True,
    }

    if request.method == "POST":
        form = UserCreationForm(inputs)
        if form.is_valid():
            user = User.objects.create_user(
                inputs["username"], None, inputs["password1"]
            )
            user.save()
            return HttpResponseRedirect(reverse("orders:login"))
        context["isValid"] = False

    return render(request, "registration/register.html", context)
