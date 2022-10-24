from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView
)

from users import views
from users.views import login


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path("login/", login, name="login"),
]
