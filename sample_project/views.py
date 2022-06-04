from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			messages.success(request, "Logedin successfully.")
			return redirect("all_notes")
		else:
			messages.warning(request, "Invalid credentials")
			return redirect('user_login')
	else:
		return render(request, 'login.html')