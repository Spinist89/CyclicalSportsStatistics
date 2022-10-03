from django.shortcuts import render


def register(request):
    return render(request, "authreg/register.html")


def login(request):
    return render(request, "authreg/login.html")
