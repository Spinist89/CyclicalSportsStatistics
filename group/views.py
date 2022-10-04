from django.shortcuts import render


def create_group(request):
    return render(request, "group/create_group.html")


def group(request):
    return render(request, "group/group.html")
