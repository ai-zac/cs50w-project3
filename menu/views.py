from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .models import Section


# Create your views here.
@login_required(redirect_field_name="")
def index(request):
    context = {
        # Order according to the number of items in each section 
        "menu": Section.objects.annotate(count=Count("section_plates")).order_by('count'),
    }
    return render(request, "menu/index.html", context)
