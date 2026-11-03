from django.urls import path

from search import views

urlpatterns = [
    path("", views.home, name="home"),
    path("terms/", views.terms, name="terms"),
]
