from GoogleProject import views
from django.urls import path, include

urlpatterns = [
    path('', views.GooglePage, name='HomePage'),
    path('terms/', views.TermsPage, name='TermsPage'),
]