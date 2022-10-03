from django.urls import path

from authreg.views import login, register

urlpatterns = [
    path("register/", register),
    path("login/", login),
]
