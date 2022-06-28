
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *
from django.db.models import Q


def inicio(request):

    return render(request, "MiniBlogApp/index.html", {})

# def base(request):
    
#     return render(request, "MiniBlogApp/base.html", {})