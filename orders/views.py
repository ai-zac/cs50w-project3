from django.http import HttpResponse
from django.shortcuts import render

from .models import Plate

# Create your views here.
def index(request):
    context = {
        "Subs": Plate.objects.filter(section__name="Subs")
    }
    return render(request, "orders/index.html", context)
