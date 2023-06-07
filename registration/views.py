from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect

from django.urls import reverse
from .forms import LoginForm, RegisterForm

# Create your views here.
@login_required(redirect_field_name="")
def accounts(request):
    return HttpResponseRedirect(reverse("menu:index"))


def register(request):
    context = {
        "form": RegisterForm(),
        "isValid": True,
    }

    if request.method == "POST":
        form = RegisterForm(request.POST)

        # If something is incorrect, register the user
        if (
            not form.is_valid()
            or User.objects.filter(username__iexact=request.POST["username"]).exists()
            or request.POST["password"] != request.POST["password_confirm"]
        ):
            context["isValid"] = False
            return render(request, "registration/register.html", context)

        # Else, redirect again register's form
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = User.objects.create_user(username, None, password)
        user.save()

        return HttpResponseRedirect(reverse("registration:login"))

    return render(request, "registration/register.html", context)


def login(request):
    context = {
        "form": LoginForm,
        "isValid": True,
    }

    if request.method == "POST":
        form = LoginForm(request.POST)

        # If all pass, login the user
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(reverse("menu:index"))

        # else, redirect again login's form
        context["isValid"] = False
        return render(request, "registration/login.html", context)

    return render(request, "registration/login.html", context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("registration:login"))
