from django.shortcuts import render


def home(request):
    return render(request, 'main/index.html')


def terms(request):
    return render(request, 'main/terms_page.html')