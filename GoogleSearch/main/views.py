from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/home.html')

def terms_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/terms.html')