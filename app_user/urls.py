from django.urls import path, include
from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path("register/", view=views.RegisterUser, name="register_user-page"),
    path("profile/", view=views.Profile, name="profile-page"),
    path("about-user/", view=views.AboutUser, name='about_user-page')
]