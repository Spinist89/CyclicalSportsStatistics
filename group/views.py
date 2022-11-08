from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import GroupForm
from .models import Group, User


@login_required
def create_group(request, user=None):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.coach = request.user
        new_group.sportsmen = request.user


        new_group.save()
        form.save_m2m()
        return redirect("start_page:index")
    return render(request, 'group/create_group.html', {'form': form})


@login_required
def group(request):
    groups = Group.objects.filter(coach=request.user)
    print(groups)
    return render(request, "group/group.html", {"groups":groups})
