from django.shortcuts import render


def create_training(request):
    return render(request, "training/create_training.html")


def training(request):
    return render(request, "training/training.html")
