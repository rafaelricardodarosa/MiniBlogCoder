from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def post(request):
    return HttpResponse("Hello World")