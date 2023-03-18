from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from app_user.forms import *
from django.contrib import messages

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
			return redirect("app_general:home-page")
	else:
		form = RegisterUserForm()
	context = {"form": form}
	return render(request, "registration/register.html", context)