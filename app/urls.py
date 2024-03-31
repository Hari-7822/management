from django.urls import path
from django.contrib.auth.views import LoginView
from . import auth, views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="login.j2"), name="login"),
    path("signup/", auth.signup, name="signup")
]