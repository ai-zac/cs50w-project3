from django.http import HttpResponse
from django.shortcuts import render

from .models import Item

# Create your views here.
def index(request):
    context = {
        "menu": Item.objects.get()
    }
    return render(request, "orders/index.html", context)
