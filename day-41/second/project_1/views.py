from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    return render(request,'index.html')
def About(request):
    return HttpResponse("<h1>This iS 2nd Project About Page</h1>")
