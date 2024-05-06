from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home1(request):
    return HttpResponse("<h1>This iS Project 2 Home page</h1>")
def About1(request):
    return HttpResponse("<h1>This iS Project 2 About page</h1>")
