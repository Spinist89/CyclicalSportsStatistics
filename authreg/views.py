from django.shortcuts import render

def authreg(request):
    return render(request, 'authreg/index.html')
