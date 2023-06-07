from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "orders/index.html")
