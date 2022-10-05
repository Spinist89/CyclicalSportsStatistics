from django.shortcuts import render


def sportsmen_statistic(request):
    return render(request, "statistic/sportsmen_statistic.html")


def coach_statistic(request):
    return render(request, "statistic/coach_statistic.html")