from django.http import HttpResponse
from django.shortcuts import render

from .models import Menu

# Create your views here.
def index(request):
    context = {
        "menu": Menu.objects.all()
    }
    return render(request, "orders/index.html", context)
