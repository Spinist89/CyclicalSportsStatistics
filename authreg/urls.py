from django.urls import path

from authreg.views import login, register

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
]
