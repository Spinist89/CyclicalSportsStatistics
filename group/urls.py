from django.urls import path

from group.views import create_group, group

app_name = "group"

urlpatterns = [
    path("create_group/", create_group, name="create_group"),
    path("group/", group, name="group"),
]
