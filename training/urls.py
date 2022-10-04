from django.urls import path

from training.views import create_training, training

urlpatterns = [
    path("create_training/", create_training, name="create_training"),
    path("training/", training, name="training"),
]
