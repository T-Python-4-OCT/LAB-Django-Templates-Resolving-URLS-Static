from django.shortcuts import render
from django.http import HttpResponse,HttpRequest


# Create your views here.


def home(request:HttpRequest):
    
    return render(request,'main/home.html')                

def terms(request:HttpRequest):
    return render(request, "main/terms.html")