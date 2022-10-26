from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("start_page.urls", namespace="start_page")),
    path("auth/", include("users.urls",  namespace='users')),
    path("auth/", include("django.contrib.auth.urls")),
    path("group/", include("group.urls",  namespace='group')),
    path("training/", include("training.urls",  namespace='training')),
    path("statistic/", include("statistic.urls",  namespace='statistic')),
]
