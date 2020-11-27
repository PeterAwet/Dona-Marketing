from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
	return render(request,'accounts/profile.html',{})

def login(request):
	return render(request,'account/login.html',{})

def about(request):
	return render(request,'accounts/about.html',{})