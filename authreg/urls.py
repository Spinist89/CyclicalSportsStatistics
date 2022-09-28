from django.urls import path

from authreg.views import register

urlpatterns = [
    path('register/', register),
    
    ]