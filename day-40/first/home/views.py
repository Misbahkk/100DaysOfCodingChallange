from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return HttpResponse("<h1>Home</h1>")
def About(request):
    return HttpResponse("<h1>about</h1>")