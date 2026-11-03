from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def GooglePage(request: HttpRequest):
    return render(request, 'index.html')

def TermsPage(request: HttpRequest):
    return render(request, 'terms.html')