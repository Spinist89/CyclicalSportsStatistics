from django.shortcuts import render
from django.views.generic import CreateView


from .forms import CreationForm



def login(request):
    return render(request, "users/login.html")

class SignUp(CreateView):
    form_class = CreationForm
    template_name = 'users/signup.html'