from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from app_user.forms import *
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.


def RegisterUser(request):
	if request.method == "POST":
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			data_username = form.cleaned_data["username"]
			data_password = form.cleaned_data["password1"]
			user = authenticate(username=data_username, password=data_password)
			login(request, user)
			messages.success(request, ("Registration Successful"))
			return HttpResponseRedirect(reverse("app_general:home-page"))
	else:
		form = RegisterUserForm()
	context = {"form": form}
	return render(request, "app_user/register.html", context)


@login_required
def Profile(request):
	if request.method == "POST":
		form = UserForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("app_user:profile-page"))
	else:
		form = UserForm(instance=request.user)
	context = {"form": form}
	return render(request, "app_user/profile.html", context)