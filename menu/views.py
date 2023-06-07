from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .models import Plate, Section


# Create your views here.
@login_required(redirect_field_name="")
def index(request):
    context = {
        "menu": Section.objects.all(),
    }
    return render(request, "menu/index.html", context)
