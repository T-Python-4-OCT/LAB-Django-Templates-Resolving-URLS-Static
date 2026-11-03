from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("terms/", TemplateView.as_view(template_name="terms.html"), name="terms"),
]
