from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import GroupForm
from users.models import Group, User


@login_required
def create_group(request):
    # return render(request, "group/create_group.html")
    form = GroupForm(request.POST or None)
    if form.is_valid():
        new_group = form.save(commit=False)
        new_group.coach = request.user
        new_group.title = f"{request.user.username}_{form.cleaned_data['title']}"
        new_group.save()
        return redirect("start_page:index")
    return render(request, 'group/create_group.html', {'form': form})


@login_required
def group(request):
    groups = Group.objects.all()
    sportsmens = User.objects.filter(group=request.user.group).all()
    context = {"groups":groups,
               "sportsmens":sportsmens,}
    return render(request, "group/group.html", context)
