from django.urls import path

from statistic.views import sportsmen_statistic, coach_statistic

app_name = 'statistic'

urlpatterns = [
    path("sportsmen_statistic/", sportsmen_statistic, name="sportsmen_statistic"),
    path("coach_statistic/", coach_statistic, name="coach_statistic"),
]