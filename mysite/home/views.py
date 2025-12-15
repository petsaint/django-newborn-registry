from django.shortcuts import render
from .models import Newborn


def newborn_list(request):
    newborns = Newborn.objects.all()
    return render(request, "home/newborn_list.html", {
        "newborns": newborns
    })
