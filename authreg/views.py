from django.shortcuts import render
from django.http import HttpResponse

def authreg(request):
    return HttpResponse('<h1>Авторизация, Регистрация</h1>')