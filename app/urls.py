from django.urls import path
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

from . import auth, views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="forms/login.j2"), name="login"),
    path("signup/", auth.signup, name="signup")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)