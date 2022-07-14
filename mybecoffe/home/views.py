from datetime import date, datetime, time
from multiprocessing import context
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from .models import PresenceTimes
from django.contrib.auth.models import User

# Create your views here.
def home(request):
	print("home view")
	return render(request, 'home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")

def arrival(request):
	if request.method == "POST":
		now = datetime.now()
		presence = PresenceTimes.objects.filter(user=request.user, date=now)
		if not presence:
			PresenceTimes.objects.create(user=request.user,date=now,arrival=now).save()
			messages.success(request, "Succesfully reported arrival time." )
		else:
			messages.error(request, "Arrival time has already been reported." )
			return redirect("home")
		return redirect("home")
	

def departure(request):
	if request.method == "POST":
		now = datetime.now()
		presence = PresenceTimes.objects.get(user=request.user, date=now)
		if presence:
			if presence.departure == None:
				presence.departure = now
				presence.save()
				messages.info(request, "Succesfully reported departure time.")
			else:
				messages.error(request, "Departure time has already been reported.")
				return redirect("home")
		else:
			messages.error(request, "Must report arrival time first." )
			return redirect("home")

		return redirect("home")


