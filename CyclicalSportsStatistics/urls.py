from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("start_page.urls")),
    path("auth/", include("authreg.urls")),
    path("group/", include("group.urls")),
    path("training/", include("training.urls")),
]
