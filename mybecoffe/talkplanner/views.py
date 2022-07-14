from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TalkForm
from .models import Talks

@login_required(login_url='access')
def index(request):
	item_list = Talks.objects.order_by("date")

	if request.method == "POST":
		form = TalkForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data["user"]
			if user == request.user:
				form.save()
				return redirect('talkplanner')
			else:
				messages.error("Please select yourself as the user")
				return redirect('talkplanner')
	form = TalkForm()

	page = {
			"forms" : form,
			"list" : item_list,
			"title" : "Talks list",
		}
	return render(request, 'talkplanner.html', page)

def remove(request, item_id):
	item = Talks.objects.get(id=item_id)
	is_user = request.user == item.user
	if is_user:
		if request.method == "POST":
			item.delete()
			return redirect('talkplanner')
	else: 
		messages.error("The post you tried to delete isnt yours")
		return redirect('talkplanner')
	return render(request,'talkplanner.html')