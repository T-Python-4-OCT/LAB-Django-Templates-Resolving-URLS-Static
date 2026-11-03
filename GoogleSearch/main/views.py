from django.http import HttpRequest
from django.shortcuts import render


def home_view(request: HttpRequest):
    return render(request, "main/index.html")


def terms_view(request: HttpRequest):
    return render(request, "main/terms.html")
# Create your views here.
